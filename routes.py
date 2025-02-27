from flask import render_template, request, jsonify
from google.genai import types

DEFAULT_RESPONSES = {
    "Text-Correct": "Przykładowa poprawiona wersja tekstu.",
    "Summarizer": "Przykładowe podsumowanie tekstu.",
    "Code-Reviewer": "Przykładowa recenzja kodu.",
    "Translate": "Example translated text."
}

def init_routes(app, client, agents, sys_instruct):
    """Inicjalizuje trasy Flask."""

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/change_agent', methods=['POST'])
    def change_agent():
        """Zmienia aktualnego agenta i ustawia przykładowy output."""
        nonlocal sys_instruct
        data = request.get_json()
        new_agent = data.get("agent", "")
        if new_agent in agents:
            sys_instruct = agents[new_agent]
            return jsonify({
                "message": f"Agent zmieniony na: {new_agent}",
                "example_output": DEFAULT_RESPONSES.get(new_agent, "Brak przykładowego tekstu.")
            })
        return jsonify({"message": "Nie znaleziono takiego agenta."})

    @app.route('/process', methods=['POST'])
    def process():
        """Przetwarza tekst za pomocą API Google."""
        if not client:
            return jsonify({"corrected_text": "Błąd: Brak połączenia z API."})

        data = request.get_json()
        input_text = data.get("text", "")
        temperature = float(data.get("temperature", 0.5))
        max_tokens = int(data.get("max_output_tokens", 512))

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=input_text,
                config=types.GenerateContentConfig(
                    max_output_tokens=max_tokens,
                    temperature=temperature,
                    system_instruction=sys_instruct
                )
            )
            corrected_text = str(response.text) if response.candidates else "Błąd przetwarzania."
        except Exception as e:
            corrected_text = f"Błąd API: {e}"

        return jsonify({"corrected_text": corrected_text})

