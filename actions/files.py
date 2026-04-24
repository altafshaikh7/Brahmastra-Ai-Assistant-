import os

def open_file(path):
    try:
        os.startfile(path)
        return f"Opening file {path}"
    except:
        return "File not found"

def list_files(directory):
    try:
        files = os.listdir(directory)
        return ", ".join(files[:10])
    except:
        return "Directory not found"