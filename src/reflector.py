import logging

class Reflector:
    def __init__(self, llm, reflection_prompt_template, solving_prompt_template):
        self.llm = llm
        self.reflection_prompt_template = reflection_prompt_template
        self.solving_prompt_template = solving_prompt_template
        self.logger = logging.getLogger(__name__)

    def reflect(self, output, question):
        prompt = self.reflection_prompt_template.format(output=output, question=question)
        return self.llm.generate_response(prompt)

    def solve(self, problems, output, question):
        prompt = self.solving_prompt_template.format(problems=problems, output=output, question=question)
        return self.llm.generate_response(prompt)
