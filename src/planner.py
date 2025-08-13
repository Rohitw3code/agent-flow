import logging
import json
import re
from src.llm_client import LLMClient

logger = logging.getLogger(__name__)

class Planner:
    def __init__(self):
        self.llm = LLMClient()

    def plan(self, question: str):
        logger.info("Planning tasks for question: %s", question)

        system_prompt = """
You are a planning AI.
You MUST output a valid JSON object with this structure only:
{
  "plan": [
    {"task": "string", "tool": "string"}
  ]
}
No explanations, no extra text outside the JSON.
"""

        user_prompt = f"""
Question: {question}

Break this question into a series of steps.
Assign each step to a tool name that could handle it.
Example tools: WikipediaTool, CalculatorTool, SearchTool
"""

        response = self.llm.chat(system_prompt, user_prompt)

        try:
            plan_data = self._parse_json_safe(response)
            logger.info("Parsed plan: %s", plan_data)
            return plan_data
        except Exception as e:
            logger.error("Failed to parse plan JSON: %s", e)
            return {"plan": []}

    def _parse_json_safe(self, text: str):
        """
        Try parsing JSON output from the LLM, 
        cleaning common formatting issues (markdown, extra text, etc.)
        """
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            # Remove Markdown code fences
            cleaned = re.sub(r"```(json)?", "", text).strip()

            # Try to extract first {...} JSON block if extra text exists
            json_match = re.search(r"\{.*\}", cleaned, re.DOTALL)
            if json_match:
                return json.loads(json_match.group(0))

            # Last attempt
            return json.loads(cleaned)
