import json
from datetime import datetime
from config import TOKEN_PATH, LOG_PATH, AGENTS_PATH

def get_token():
    """Pobiera token API z pliku."""
    with open(TOKEN_PATH, "r") as file:
        data = json.load(file)
    return data.get("token_Gemini")

def save_log(text):
    """Zapisuje logi do pliku."""
    with open(LOG_PATH, "a", encoding="utf-8") as file:
        current_date = datetime.today().strftime('%Y-%m-%d')
        file.write(f"{current_date} | {text}\n")

def get_agents():
    """Pobiera konfigurację agentów z pliku."""
    with open(AGENTS_PATH, "r", encoding="utf-8") as file:
        return json.load(file)
