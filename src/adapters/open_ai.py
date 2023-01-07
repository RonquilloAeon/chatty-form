import openai


class OpenAi:
    def __init__(
        self,
        api_key: str,
        engine: str = "text-davinci-003",
        temperature: float = 0.6,
        max_tokens: int = 150,
    ):
        openai.api_key = api_key
        self._engine = engine
        self._temperature = temperature
        self._max_tokens = max_tokens

    def ask(self, text: str) -> str:
        response = openai.Completion.create(
            engine=self._engine,
            prompt=text,
            temperature=self._temperature,
            max_tokens=self._max_tokens,
        )

        return response.choices[0].text
