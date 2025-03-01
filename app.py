from flask import Flask
from routes import Routes
from utils import Utils
from google_client import GoogleClient

class App:
    def __init__(self):
        self.app = Flask(__name__, static_folder="static", template_folder=".")
        self.token = Utils.get_token()
        self.client = GoogleClient(api_key=self.token)
        self.agents = Utils.get_agents()
        self.sys_instruct = self.agents.get("Text-Correct", "")
        Routes.init_routes(self.app, self.client, self.agents, self.sys_instruct)

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    App().run()