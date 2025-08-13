import logging

class Planner:
    def __init__(self, llm, prompt_template):
        self.llm = llm
        self.prompt_template = prompt_template
        self.logger = logging.getLogger(__name__)

    def generate_plan(self, question):
        prompt = self.prompt_template.format(question=question)
        return self.llm.generate_response(prompt)
