import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Возвращает список словарей по заданным словам"""
    new_data = []
    for word in search.split(","):
        pattern = re.compile(word, re.IGNORECASE)
        for info in data:
            if pattern.search(str(info.get("description"))):
                new_data.append(info)
    return new_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Создает словарь, где категории - это ключ, а количество операций в каждой категории - значение словаря"""
    new_dict = {}
    new_data = []
    for category in categories:
        for operation in data:
            if operation.get("description") == category:
                new_data.append(operation.get("description"))
                new_dict = Counter(new_data)
            else:
                continue
    return new_dict
