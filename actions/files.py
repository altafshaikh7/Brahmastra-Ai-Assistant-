import os
import platform
import subprocess

def open_file(path):
    try:
        if not os.path.exists(path):
            return "File exist nahi karta"

        system = platform.system()

        if system == "Windows":
            os.startfile(path)
        elif system == "Darwin":  # macOS
            subprocess.call(["open", path])
        else:  # Linux
            subprocess.call(["xdg-open", path])

        return f"Opening file {path}"

    except Exception as e:
        print("Error:", e)
        return "File open nahi ho paya"