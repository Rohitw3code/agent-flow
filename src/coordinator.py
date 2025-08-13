import logging
from src.planner import Planner
from src.tools.wikipedia_tool import WikipediaTool
from src.tools.calculator_tool import CalculatorTool

logger = logging.getLogger(__name__)

class Coordinator:
    def __init__(self):
        self.planner = Planner()
        # Available tools
        self.tools = {
            "WikipediaTool": WikipediaTool(),
            "CalculatorTool": CalculatorTool()
        }

    def run(self, question: str):
        logger.info("Processing question: %s", question)

        plan = self.planner.plan(question)

        results = []
        for step in plan.get("plan", []):
            task = step.get("task")
            tool_name = step.get("tool")

            tool = self.tools.get(tool_name)
            if not tool:
                logger.warning("Tool %s not found. Skipping.", tool_name)
                continue

            logger.info("Executing task: %s with %s", task, tool_name)
            try:
                result = tool.run(task)
                results.append({"task": task, "result": result})
            except Exception as e:
                logger.error("Error running tool %s: %s", tool_name, e)

        return results
