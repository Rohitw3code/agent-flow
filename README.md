# Self-Reflecting LLM Agent

This is a Python-based agent that uses an LLM to plan, execute, reflect, and refine answers to user questions.

## Features
- Modular design with separation of concerns.
- Configurable prompts and LLM settings via YAML.
- Logging for traceability.
- Iterative reflection to fix issues in outputs.
- Supports OpenAI API (extensible to others).

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set `OPENAI_API_KEY` environment variable.
3. Run: `python main.py --question "Your question"`

## Configuration
Edit `config.yaml` for prompts, model, max iterations, etc.

## Testing
Run tests: `pytest tests/`
