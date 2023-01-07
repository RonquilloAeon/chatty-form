import os

from src.adapters.open_ai import OpenAi


def main():
    ai = OpenAi(os.getenv("OPENAI_KEY"), max_tokens=500)

    while True:
        request = input("Ask me!:")

        if request:
            print(ai.ask(f"{request} (as json schema)"))
        else:
            print("Enter a value!")
