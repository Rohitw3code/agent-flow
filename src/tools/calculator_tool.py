class CalculatorTool:
    """
    A basic calculator tool for evaluating math expressions.
    """
    def run(self, expression: str) -> str:
        try:
            result = eval(expression, {"__builtins__": None}, {})
            return f"Result: {result}"
        except Exception as e:
            return f"Calculation error: {e}"
