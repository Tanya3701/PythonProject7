import json
import logging
from typing import Any


logger = logging.getLogger("utils.py")
file_handler = logging.FileHandler(
    filename=r"PythonProject7\logs\utils.log", encoding="utf-8", mode="w"
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def json_read_file(json_file: Any) -> list[dict[dict[dict]]]:
    """Преобразует Json файл в список"""
    try:
        logger.info("Запрашиваем файл")
        with open(json_file, "r", encoding="utf-8") as file:
            try:
                operations = json.load(file)
            except json.decoder.JSONDecodeError:
                operations = []
                logger.error("Неверный формат")
    except FileNotFoundError:
        logger.error("Файл не найден")
        operations = []
    logger.info("Файл успешно преобразован")
    return operations


if __name__ == "__main__":
    print(json_read_file("data/operations.json"))
