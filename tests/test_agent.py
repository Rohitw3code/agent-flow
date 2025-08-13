import pytest
from src.agent import SelfReflectingAgent
import yaml

@pytest.fixture
def config():
    with open('../config.yaml', 'r') as f:
        return yaml.safe_load(f)

def test_agent_tool_execution(config):
    class MockLLM:
        def generate_response(self, prompt):
            if "Available tools" in prompt:
                return '[{"tool": "WikipediaTool", "query": "Get population of France"}]'
            elif "Results" in prompt:
                return "Final answer: 67 million"
            elif "Check" in prompt:
                return "No issues detected."
            return ""

    config['llm']['model'] = "mock"
    agent = SelfReflectingAgent(config)
    agent.llm = MockLLM()
    output = agent.run("What is the population of France?")
    assert "67 million" in output
