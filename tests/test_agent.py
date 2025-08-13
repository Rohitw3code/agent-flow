import pytest
from src.agent import SelfReflectingAgent
import yaml

@pytest.fixture
def config():
    with open('../config.yaml', 'r') as f:
        return yaml.safe_load(f)

def test_agent_simple_question(config, monkeypatch):
    class MockLLM:
        def generate_response(self, prompt):
            if "plan" in prompt.lower():
                return "Step 1: Recall geography. Step 2: Answer."
            elif "execute" in prompt.lower():
                return "Paris"
            elif "check" in prompt.lower():
                return "No issues detected."
            return ""

    config['llm']['model'] = "mock"
    agent = SelfReflectingAgent(config)
    agent.llm = MockLLM()
    output = agent.run("What is the capital of France?")
    assert "Paris" in output

def test_agent_with_reflection(config, monkeypatch):
    class MockLLM:
        call_count = 0
        def generate_response(self, prompt):
            self.call_count += 1
            if "plan" in prompt.lower():
                return "Step 1: Calculate. Step 2: Answer."
            elif "execute" in prompt.lower():
                return "5"
            elif "check" in prompt.lower():
                return "Error: 2+2 is 4, not 5."
            elif "correct" in prompt.lower():
                return "4"
            return ""

    config['llm']['model'] = "mock"
    agent = SelfReflectingAgent(config)
    agent.llm = MockLLM()
    output = agent.run("What is 2+2?")
    assert "4" in output
