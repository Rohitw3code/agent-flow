import logging
import openai
import os

class LLMInterface:
    def __init__(self, model, temperature):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.temperature = temperature
        self.logger = logging.getLogger(__name__)

    def generate_response(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            self.logger.error(f"LLM API error: {e}")
            raise
