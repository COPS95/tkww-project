import os
import yaml
import pickle
from typing import Any


def load_file(path: str, file_name: str) -> Any:
    """Load a file from the specified path.

    Args:
        path (str): The path to the directory where the file is located.
        file_name (str): The name of the file to be loaded.

    Returns:
        Any: The loaded file object.

    Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: If there is an error while loading the file.
    """
    full_path = os.path.join(path, file_name)
    try:
        with open(full_path, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None
    except Exception as e:
        return None


def load_logging_config(path: str) -> dict:
    """
    Load the logging configuration from a YAML file.

    Args:
        path (str): The path to the YAML file containing the logging configuration.

    Returns:
        dict: The loaded logging configuration as a dictionary.
    """
    try:
        with open(path, "rt") as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise RuntimeError(f"Failed to load logging configuration: {e}")
