from typing import Any

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
]


def filter_by_currency(transactions_some: list[dict], currency: str) -> Any:
    """Функция фильтра данных по видам валюты"""
    transactions_list = []
    for transaction in transactions_some:
        if transaction.get("operationAmount") is not None:
            if transaction.get("operationAmount").get("currency") is not None:
                key = transaction.get("operationAmount").get("currency").get("code")
                if key == currency:
                    transactions_list.append(transaction)
        else:
            key = transaction.get("currency_code")
            if key == currency:
                transactions_list.append(transaction)
    return transactions_list


def transaction_descriptions(transactions_some: list[dict]) -> Any:
    """Генератор возвращает тип операции"""
    for transaction in transactions_some:
        description = transaction.get("description")
        yield description


def card_number_generator(start: int, stop: int) -> Any:
    """Генерирует номера карт"""
    if start > 0 and stop <= 9999999999999999:
        z = start
        x = 10000000000000001
        while z <= stop:
            yield f"{str(x)[1:5]} {str(x)[5:9]} {str(x)[9:13]} {str(x)[13:17]}"
            x += 1
            z += 1
    else:
        raise ValueError("Карты с таким номером не существует")
