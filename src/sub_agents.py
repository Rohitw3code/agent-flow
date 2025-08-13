import logging

class WikipediaTool:
    def run(self, query):
        if "population of france" in query.lower():
            return "67 million"
        elif "world population" in query.lower():
            return "8 billion"
        return "Data not found"

class CalculatorTool:
    def run(self, expression):
        try:
            return str(eval(expression))
        except Exception as e:
            return f"Error: {e}"

class SubAgentManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.tools = {
            "WikipediaTool": WikipediaTool(),
            "CalculatorTool": CalculatorTool(),
        }

    def execute_step(self, step):
        tool_name = step.get("tool")
        query = step.get("query")
        if tool_name in self.tools:
            self.logger.info(f"Executing step with {tool_name}: {query}")
            return self.tools[tool_name].run(query)
        else:
            return f"Tool {tool_name} not available"
