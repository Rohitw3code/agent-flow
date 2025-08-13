# Self-Reflecting Multi-Agent LLM Agent

This project extends the self-reflecting agent with multiple sub-agents and tool-based execution.

## Features
- Planner generates structured steps, each assigned to a sub-agent/tool.
- Executor calls only available sub-agents.
- Reflection to verify and correct final output.

## Tools Implemented
- WikipediaTool (dummy data for now)
- CalculatorTool

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set `GROQ_API_KEY` (for Groq LLaMA) or `OPENAI_API_KEY`.
3. Run: `python main.py --question "Your question"`

## Testing
Run tests: `pytest tests/`
