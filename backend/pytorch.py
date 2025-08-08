from typing import Any, Dict


class PyTorchBackend:
    def __init__(self):
        pass

    async def generate(self, model: str, prompt: str, model_kwargs: Dict[str, Any]):
        """LLM Inference using PyTorch as backend.

        Args:
            model (str): The model to use for text generation.
            prompt (str): The prompt to use for text generation.
            model_kwargs (Dict[str, Any]): Additional model parameters.
        """

        pass
