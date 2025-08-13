import argparse
import logging
import yaml
from src.agent import SelfReflectingAgent
from src.utils import setup_logging

def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Self-Reflecting LLM Agent")
    parser.add_argument("--question", required=True, help="The question or problem to solve")
    args = parser.parse_args()

    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    agent = SelfReflectingAgent(config)
    final_output = agent.run(args.question)
    print("\nFinal Output:")
    print(final_output)

if __name__ == "__main__":
    main()
