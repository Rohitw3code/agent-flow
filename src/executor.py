import logging

class Executor:
    def __init__(self, llm, prompt_template):
        self.llm = llm
        self.prompt_template = prompt_template
        self.logger = logging.getLogger(__name__)

    def execute_plan(self, question, plan):
        prompt = self.prompt_template.format(plan=plan, question=question)
        return self.llm.generate_response(prompt)
