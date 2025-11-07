import json
from typing import Any


def json_read_file(json_file: Any) -> list[dict[dict[dict]]]:
    """Преобразует Json файл в список"""
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            try:
                operations = json.load(file)
            except json.decoder.JSONDecodeError:
                operations = []
    except FileNotFoundError:
        operations = []
    return operations
