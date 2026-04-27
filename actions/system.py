import os
from datetime import datetime

def get_time():
    return f"Current time is {datetime.now().strftime('%H:%M')}"

def volume_up():
    try:
        os.system("nircmd.exe changesysvolume 2000")
        return "Volume increased"
    except:
        return "Volume control failed"

def volume_down():
    try:
        os.system("nircmd.exe changesysvolume -2000")
        return "Volume decreased"
    except:
        return "Volume control failed"

def shutdown(confirm=False):
    if confirm:
        os.system("shutdown /s /t 1")
        return "Shutting down system"
    return "Please confirm shutdown"

def restart(confirm=False):
    if confirm:
        os.system("shutdown /r /t 1")
        return "Restarting system"
    return "Please confirm restart"