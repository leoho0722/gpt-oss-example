import argparse


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
        "--user-prompt",
        type=str,
        help="The user prompt to use for the example.",
    )
    parser.add_argument(
        "--backend",
        type=str,
        required=True,
        choices=["pytorch", "ollama"],
        help="The backend to use for the example.",
    )
    parser.add_argument(
        "--ollama-host",
        type=str,
        default="http://localhost:11434",
        help="The host for the Ollama backend.",
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
        "--verbose",
        action="store_true",
        default=False,
        help="Enable verbose output.",
    )
    return parser.parse_args()


def main(args: argparse.Namespace):
    model: str = args.model
    prompt_filepath: str = args.prompt_filepath
    user_prompt: str = args.user_prompt
    backend: str = args.backend
    ollama_host: str = args.ollama_host
    context_length: int = args.context_length
    temperature: float = args.temperature
    verbose: bool = args.verbose

    if verbose:
        print(f"Model: {model}")
        print(f"Prompt Filepath: {prompt_filepath}") if prompt_filepath else None
        print(f"User Prompt: {user_prompt}") if user_prompt else None
        print(f"Backend: {backend}")
        print(f"Ollama Host: {ollama_host}") if backend == "ollama" else None
        print(f"Context Length: {context_length}")
        print(f"Temperature: {temperature}")


if __name__ == "__main__":
    args = parse_args()

    main(args)
