import json
from typing import Any, Dict


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


def read_prompt_json(file_path: str) -> Dict[str, Any]:
    """Read the prompt from a JSON file.

    Args:
        file_path (str): The path to the prompt JSON file.

    Returns:
        content (Dict[str, Any]): The content of the prompt JSON file or an error message.
    """

    try:
        with open(file_path, "r") as file:
            return json.loads(file.read())
    except FileNotFoundError:
        print(f"Prompt JSON file '{file_path}' not found.")
        return {"error": "File not found"}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file '{file_path}'.")
        return {"error": "Invalid JSON"}
    except Exception as e:
        print(f"An error occurred while reading the prompt JSON file: {e}")
        return {"error": "Unknown error"}
