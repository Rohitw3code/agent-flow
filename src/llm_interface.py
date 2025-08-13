# src/llm_interface.py

import logging
import os
from groq import Groq

class LLMInterface:
    def __init__(self, model="llama3-70b-8192", temperature=0.7):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
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
            self.logger.error(f"Groq API error: {e}")
            raise
