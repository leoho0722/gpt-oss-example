def read_prompt_file(file_path: str) -> str:
    """Read the prompt from a file.

    Args:
        file_path (str): The path to the prompt file.

    Returns:
        str: The content of the prompt file or an error message.
    """

    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Prompt file '{file_path}' not found.")
        return ""
    except Exception as e:
        print(f"An error occurred while reading the prompt file: {e}")
        return ""
