import os

SAVE_DIR = "saved_qadl_files"
os.makedirs(SAVE_DIR, exist_ok=True)  # Ensure the save directory exists

def list_saved_qadl_files():
    """Lists available QADL files in the saved directory."""
    files = [f for f in os.listdir(SAVE_DIR) if f.endswith(".qadl")]
    return files if files else ["⚠️ No saved QADL files found."]

def open_qadl_file(file_name):
    """Reads a QADL script from a selected file."""
    file_path = os.path.join(SAVE_DIR, file_name)
    
    if not os.path.exists(file_path):
        return "", "⚠️ File not found!"
    
    try:
        with open(file_path, "r") as file:
            return file.read(), f"✅ File '{file_name}' loaded successfully!"
    except Exception as e:
        return "", f"❌ Error loading file: {str(e)}"

def save_qadl_file(content, filename):
    """Saves a QADL script to a specified file."""
    if not filename.endswith(".qadl"):
        filename += ".qadl"
    
    file_path = os.path.join(SAVE_DIR, filename)
    
    try:
        with open(file_path, "w") as file:
            file.write(content)
        return f"✅ File '{filename}' saved successfully!"
    except Exception as e:
        return f"❌ Error saving file: {str(e)}"
