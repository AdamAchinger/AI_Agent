from google import genai

class GoogleClient:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key) if api_key else None

    def generate_content(self, input_text, temperature=0.5, max_tokens=512, sys_instruct=""):
        if not self.client:
            return "Błąd: Brak połączenia z API."
        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=input_text,
                config=genai.types.GenerateContentConfig(
                    max_output_tokens=max_tokens,
                    temperature=temperature,
                    system_instruction=sys_instruct
                )
            )
            return str(response.text) if response.candidates else "Błąd przetwarzania."
        except Exception as e:
            return f"Błąd API: {e}"
