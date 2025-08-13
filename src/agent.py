import logging
from src.llm_interface import LLMInterface
from src.planner import Planner
from src.executor import Executor
from src.reflector import Reflector

class SelfReflectingAgent:
    def __init__(self, config):
        self.config = config
        self.llm = LLMInterface(config['llm']['model'], config['llm']['temperature'])
        self.planner = Planner(self.llm, config['prompts']['planning'])
        self.executor = Executor(self.llm, config['prompts']['execution'])
        self.reflector = Reflector(self.llm, config['prompts']['reflection'], config['prompts']['solving'])
        self.max_iterations = config['agent']['max_reflection_iterations']
        self.logger = logging.getLogger(__name__)

    def run(self, question):
        self.logger.info(f"Processing question: {question}")
        available_tools = ["WikipediaTool", "CalculatorTool"]
        plan = self.planner.generate_plan(question, available_tools)
        self.logger.debug(f"Generated plan: {plan}")
        output = self.executor.execute_plan(question, plan)
        self.logger.debug(f"Initial output: {output}")

        iteration = 0
        while iteration < self.max_iterations:
            problems = self.reflector.reflect(output, question)
            self.logger.debug(f"Reflection problems: {problems}")
            if "No issues detected" in problems:
                self.logger.info("No issues found. Returning output.")
                return output
            output = self.reflector.solve(problems, output, question)
            self.logger.debug(f"Refined output: {output}")
            iteration += 1

        self.logger.warning(f"Max iterations reached ({self.max_iterations}). Returning last output.")
        return output
