import sys
import os
import gradio as gr

# Ensure Python finds the src directory
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import QADL components
from qadl_core.qadl_executor import execute_qadl_script
from utils.file_handler import open_qadl_file, save_qadl_file

# ---------------------- QADL Execution Logic ----------------------
def run_qadl(qadl_script):
    """Executes a QADL script and returns the execution status and circuit visualization."""
    if not qadl_script.strip():
        return "⚠️ Please enter a QADL script.", None

    status, image_path = execute_qadl_script(qadl_script)

    if image_path and os.path.exists(image_path):
        return status, image_path
    return status, None

# ---------------------- Gradio UI Setup ----------------------
def open_file():
    """Opens a QADL file and returns its content."""
    return open_qadl_file()

def save_file(qadl_script, file_name="example.qadl"):
    """Saves the QADL script to a file."""
    save_qadl_file(qadl_script, file_name)
    return f"✅ File '{file_name}' saved successfully!"

# ---------------------- UI Layout ----------------------
with gr.Blocks(theme="soft") as qadl_ui:
    gr.Markdown("# 🚀 QADL: Prototype of Quantum Architecture Description")

    with gr.Row():
        with gr.Column(scale=3):
            gr.Markdown("✏️ **QADL Editor**")

            qadl_editor = gr.Textbox(
                lines=12,
                placeholder="Write your QADL script here...",
                label="QADL Script"
            )

            file_name = gr.Textbox(value="example.qadl", label="File Name")

            with gr.Row():
                open_button = gr.Button("📂 Open QADL")
                save_button = gr.Button("💾 Save QADL")

        with gr.Column(scale=2):
            gr.Markdown("🔍 **Execution Status**")
            execution_status = gr.Textbox(label="Status")

            gr.Markdown("🖼️ **Quantum Circuit**")
            circuit_image = gr.Image(label="Generated Circuit")

    run_button = gr.Button("🚀 Run QADL")

    # ---------------------- UI Events ----------------------
    open_button.click(open_file, outputs=qadl_editor)
    save_button.click(save_file, inputs=[qadl_editor, file_name], outputs=execution_status)
    run_button.click(run_qadl, inputs=qadl_editor, outputs=[execution_status, circuit_image])

# ---------------------- Start Gradio App ----------------------
if __name__ == "__main__":
    qadl_ui.launch()
