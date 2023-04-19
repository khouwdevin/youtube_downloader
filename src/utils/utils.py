import sys
import os

def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def replace_symbol(text: str):
    replace_char = ["<", ">", "/", "\\", "?", ".", ":", "|"]
    current_text = text

    for i in replace_char:
        current_text = current_text.replace(i, "")
    
    return current_text
