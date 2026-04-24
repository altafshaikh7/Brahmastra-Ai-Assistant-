import os
from datetime import datetime

def get_time():
    return f"Current time is {datetime.now().strftime('%H:%M')}"

def volume_up():
    os.system("nircmd.exe changesysvolume 2000")
    return "Volume increased"

def volume_down():
    os.system("nircmd.exe changesysvolume -2000")
    return "Volume decreased"

def shutdown():
    os.system("shutdown /s /t 1")
    return "Shutting down system"

def restart():
    os.system("shutdown /r /t 1")
    return "Restarting system"