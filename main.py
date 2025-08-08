import argparse
import asyncio

from backend.ollama import OllamaBackend
from utils.prompt import read_prompt_file


def parse_args():
    parser = argparse.ArgumentParser(
        description="A Python script for gpt-oss-example",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-m",
        "--model",
        type=str,
        required=True,
        help="""The model to use for the example (e.g., 'gpt-oss:20b', 
              'gpt-oss:120b', 'openai/gpt-oss-20b', 'openai/gpt-oss-120b').""",
    )
    parser.add_argument(
        "--prompt-filepath",
        type=str,
        help="The prompt file path to use for the example.",
    )
    parser.add_argument(
        "--system-prompt",
        type=str,
        help="The system prompt to use for the example.",
    )
    parser.add_argument(
        "--user-prompt",
        type=str,
        help="The user prompt to use for the example.",
    )
    parser.add_argument(
        "--backend",
        type=str,
        required=True,
        choices=["pytorch", "ollama", "ollama-turbo"],
        help="The backend to use for the example.",
    )
    parser.add_argument(
        "--ollama-host",
        type=str,
        default="http://localhost:11434",
        help="The host for the Ollama backend.",
    )
    parser.add_argument(
        "--ollama-turbo-apikey",
        type=str,
        help="The API key for the Ollama Turbo.",
    )
    parser.add_argument(
        "--context-length",
        type=int,
        default=8192,
        help="The context length to use for the example.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=1.0,
        help="The temperature to use for the example.",
    )
    parser.add_argument(
        "--reasoning-effort",
        type=str,
        default="medium",
        choices=["low", "medium", "high"],
        help="The reasoning effort to use for the example.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Enable verbose output.",
    )
    return parser.parse_args()


def main(args: argparse.Namespace):
    model: str = args.model
    prompt_filepath: str = args.prompt_filepath
    system_prompt: str = args.system_prompt
    user_prompt: str = args.user_prompt
    backend: str = args.backend
    ollama_host: str = args.ollama_host
    ollama_turbo_apikey: str = args.ollama_turbo_apikey
    context_length: int = args.context_length
    temperature: float = args.temperature
    reasoning_effort: str = args.reasoning_effort
    verbose: bool = args.verbose

    if verbose:
        print(f"Model: {model}")
        print(f"Prompt Filepath: {prompt_filepath}") if prompt_filepath else None
        print(f"System Prompt: {system_prompt}") if system_prompt else None
        print(f"User Prompt: {user_prompt}") if user_prompt else None
        print(f"Backend: {backend}")
        print(f"Ollama Host: {ollama_host}") if backend == "ollama" else None
        print(
            f"Ollama Turbo API Key: {ollama_turbo_apikey}"
        ) if backend == "ollama-turbo" else None
        print(f"Context Length: {context_length}")
        print(f"Temperature: {temperature}")
        print(f"Reasoning Effort: {reasoning_effort}")

    if prompt_filepath:
        prompt_file_content: str = read_prompt_file(prompt_filepath)
        prompt: str = f"{prompt_file_content}\n\nQuestion: {user_prompt}\nAnswer: "
    else:
        prompt: str = f"{system_prompt}\n{user_prompt}"

    if backend == "ollama":
        ollama_backend = OllamaBackend(host=ollama_host)
        model_kwargs = {
            "context_length": context_length,
            "temperature": temperature,
            "reasoning_effort": reasoning_effort,
        }

        asyncio.run(ollama_backend.generate(model, prompt, model_kwargs))

    if backend == "ollama-turbo":
        ollama_turbo_backend = OllamaBackend(
            host="https://ollama.com",
            header={"Authorization": f"Bearer {ollama_turbo_apikey}"},
        )
        model_kwargs = {
            "context_length": context_length,
            "temperature": temperature,
            "reasoning_effort": reasoning_effort,
        }

        asyncio.run(ollama_turbo_backend.generate(model, prompt, model_kwargs))


if __name__ == "__main__":
    args = parse_args()

    main(args)
