# main.py
import argparse
from src.coordinator import Coordinator

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", type=str, help="The question to ask the AI agent")
    args = parser.parse_args()

    question = args.question
    if not question:
        question = input("Enter your question: ")

    coordinator = Coordinator()
    result = coordinator.run(question)
    print("\nFinal Answer:\n", result)
