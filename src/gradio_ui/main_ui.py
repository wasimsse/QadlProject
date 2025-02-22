import sys
import os
import gradio as gr
from qadl_core.qadl_parser import parse_qadl
from qadl_core.qadl_executor import execute_qadl_script
from PIL import Image
import traceback
from tkinter import Tk, filedialog

# Ensure `src/` is added to sys.path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# File handling functions
def open_qadl_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("QADL Files", "*.qadl"), ("All Files", "*.*")])
    if not file_path:
        return "", "⚠️ No file selected."
    try:
        with open(file_path, "r") as f:
            content = f.read()
        return content, f"✅ File '{file_path}' loaded successfully."
    except Exception as e:
        return "", f"❌ Error loading file: {str(e)}"

def save_qadl_file(content, filename):
    if not filename:
        root = Tk()
        root.withdraw()
        filename = filedialog.asksaveasfilename(defaultextension=".qadl", filetypes=[("QADL Files", "*.qadl"), ("All Files", "*.*")])
    if not filename:
        return "❌ Save operation cancelled."
    try:
        with open(filename, "w") as f:
            f.write(content)
        return f"✅ File saved as {filename}."
    except Exception as e:
        return f"❌ Error saving file: {str(e)}"

# Function to handle QADL execution
def run_qadl(script):
    if not script.strip():
        return "⚠️ Please enter a QADL script.", None
    try:
        status, image_path = execute_qadl_script(script)
        if image_path and isinstance(image_path, str):
            img = Image.open(image_path)
            return status, img
        return status, None
    except Exception as e:
        error_msg = traceback.format_exc()
        return f"❌ Error: {str(e)}\n{error_msg}", None

# Define Gradio UI layout
with gr.Blocks(theme="soft") as qadl_ui:
    gr.Markdown("# 🚀 QADL: Quantum Circuit Editor")
    
    with gr.Row():
        with gr.Column(scale=3):
            gr.Markdown("### 📝 QADL Script Editor")
            qadl_script = gr.CodeEditor(label="QADL Script", language="python", lines=15, placeholder="Enter QADL code here...")
            
            with gr.Row():
                open_button = gr.Button("📂 Open")
                filename_input = gr.Textbox(label="Filename", placeholder="example.qadl")
                save_button = gr.Button("💾 Save")
                save_as_button = gr.Button("💾 Save As")

        with gr.Column(scale=2):
            gr.Markdown("### 🖥️ Quantum Circuit")
            output_image = gr.Image(label="Generated Circuit", type="pil")
    
    with gr.Row():
        execution_status = gr.Textbox(label="Execution Status", interactive=False, lines=2)
    
    with gr.Row():
        run_button = gr.Button("🚀 Run QADL")
        clear_button = gr.Button("🗑️ Clear")
        copy_button = gr.Button("📋 Copy Code")
        undo_button = gr.Button("↩️ Undo")
        redo_button = gr.Button("↪️ Redo")

    # Bind actions
    open_button.click(open_qadl_file, inputs=[], outputs=[qadl_script, execution_status])
    save_button.click(save_qadl_file, inputs=[qadl_script, filename_input], outputs=[execution_status])
    save_as_button.click(lambda content: save_qadl_file(content, None), inputs=[qadl_script], outputs=[execution_status])
    run_button.click(run_qadl, inputs=[qadl_script], outputs=[execution_status, output_image])
    clear_button.click(lambda: ("", None), inputs=[], outputs=[execution_status, output_image])
    copy_button.click(lambda text: text, inputs=[qadl_script], outputs=[qadl_script])
    undo_button.click(lambda text: text, inputs=[qadl_script], outputs=[qadl_script])
    redo_button.click(lambda text: text, inputs=[qadl_script], outputs=[qadl_script])

# Launch the Gradio UI
qadl_ui.launch()
