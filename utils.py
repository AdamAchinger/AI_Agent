import json
from datetime import datetime
from config import Config

class Utils:
    @staticmethod
    def get_token():
        with open(Config.TOKEN_PATH, "r") as file:
            data = json.load(file)
        return data.get("token_Gemini")

    @staticmethod
    def save_log(text):
        with open(Config.LOG_PATH, "a", encoding="utf-8") as file:
            current_date = datetime.today().strftime('%Y-%m-%d')
            file.write(f"{current_date} | {text}\n")

    @staticmethod
    def get_agents():
        with open(Config.AGENTS_PATH, "r", encoding="utf-8") as file:
            return json.load(file)