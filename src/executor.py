import logging
from src.sub_agents import SubAgentManager

class Executor:
    def __init__(self, llm, prompt_template):
        self.llm = llm
        self.prompt_template = prompt_template
        self.logger = logging.getLogger(__name__)
        self.sub_agent_manager = SubAgentManager()

    def execute_plan(self, question, plan):
        results = []
        for step in plan:
            result = self.sub_agent_manager.execute_step(step)
            results.append(result)
        combined_prompt = self.prompt_template.format(plan=plan, question=question) + f"\nResults: {results}"
        return self.llm.generate_response(combined_prompt)
