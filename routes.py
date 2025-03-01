from flask import render_template, request, jsonify

class Routes:
    DEFAULT_RESPONSES = {
        "Text-Correct": "Przykładowa poprawiona wersja tekstu.",
        "Summarizer": "Przykładowe podsumowanie tekstu.",
        "Code-Reviewer": "Przykładowa recenzja kodu.",
        "Translate": "Example translated text."
    }

    @staticmethod
    def init_routes(app, client, agents, sys_instruct):
        @app.route('/')
        def home():
            return render_template('index.html')

        @app.route('/change_agent', methods=['POST'])
        def change_agent():
            nonlocal sys_instruct
            data = request.get_json()
            new_agent = data.get("agent", "")
            if new_agent in agents:
                sys_instruct = agents[new_agent]
                return jsonify({
                    "message": f"Agent zmieniony na: {new_agent}",
                    "example_output": Routes.DEFAULT_RESPONSES.get(new_agent, "Brak przykładowego tekstu.")
                })
            return jsonify({"message": "Nie znaleziono takiego agenta."})

        @app.route('/process', methods=['POST'])
        def process():
            data = request.get_json()
            input_text = data.get("text", "")
            temperature = float(data.get("temperature", 0.5))
            max_tokens = int(data.get("max_output_tokens", 512))
            corrected_text = client.generate_content(input_text, temperature, max_tokens, sys_instruct)
            return jsonify({"corrected_text": corrected_text})
