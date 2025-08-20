from typing import Any, Dict

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


class PyTorchBackend:
    def __init__(self, model_id: str):
        """Initialize the PyTorch backend.

        Args:
            model_id (str): The model ID to load.
        """

        # Load model and tokenizer
        self._load_model_and_tokenizer(model_id)

    async def generate(self, prompt: str, model_kwargs: Dict[str, Any]):
        """LLM Inference using PyTorch as backend.

        Args:
            prompt (str): The prompt to use for text generation.
            model_kwargs (Dict[str, Any]): Additional model parameters.
        """

        pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
        )

        messages = [{"role": "user", "content": prompt}]

        output = pipe(messages, max_tokens=model_kwargs.get("context_length", 8192))
        print(output[0]["generated_text"][-1])

    def _load_model_and_tokenizer(self, model_id: str):
        """Load the model and tokenizer for text generation.

        Args:
            model_id (str): The model ID to load.
        """

        self.model = AutoModelForCausalLM.from_pretrained(
            model_id, torch_dtype="auto", trust_remote_code=True, device_map="auto"
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
