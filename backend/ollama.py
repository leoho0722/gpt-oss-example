from typing import Any, Dict, Optional

from ollama import AsyncClient, Options


class OllamaBackend:
    def __init__(self, host: str, header: Optional[Dict[str, str]] = None):
        self.client = AsyncClient(host=host, headers=header)

    async def generate(self, model: str, prompt: str, model_kwargs: Dict[str, Any]):
        """LLM Inference using Ollama as backend.

        Args:
            model (str): The model to use for text generation.
            prompt (str): The prompt to use for text generation.
            model_kwargs (Dict[str, Any]): Additional model parameters.
        """

        async for chunk in await self.client.generate(
            model=model,
            prompt=prompt,
            stream=True,
            think=True,
            keep_alive="0s",
            options=Options(
                temperature=model_kwargs.get("temperature", 0.8),
                num_ctx=model_kwargs.get("context_length", 8192),
            ),
        ):
            if not chunk.done:
                print(chunk.response, end="", flush=True)
            else:
                print("\n\ndone.")
