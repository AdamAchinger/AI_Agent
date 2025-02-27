from flask import Flask
from routes import init_routes
from utils import get_token, get_agents
from google import genai

app = Flask(__name__, static_folder="static", template_folder=".")

# Inicjalizacja agenta
default_agent = "Text-Correct"
agents = get_agents()
sys_instruct = agents.get(default_agent, "")

# Inicjalizacja klienta API Google
token = get_token()
client = genai.Client(api_key=token) if token else None

# Inicjalizacja tras
init_routes(app, client, agents, sys_instruct)

if __name__ == '__main__':
    app.run(debug=True)
