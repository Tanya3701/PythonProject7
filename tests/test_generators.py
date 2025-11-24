import pytest


from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
    transactions,
)


def test_filter_by_currency() -> None:
    """Тест корректного фильтра транзакции по заданной валюте"""
    currency_rub = filter_by_currency(transactions, "RUB")
    assert currency_rub == [
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
    ]


def test_filter_by_no_currency(fixture_filter_by_currency_usd):
    """Тест на отсутствие заданной валюты"""
    currency_rub = filter_by_currency(fixture_filter_by_currency_usd, "RUB")
    assert currency_rub == []


def test_filter_by_not_currency():
    """Тест пустой список"""
    currency_rub = filter_by_currency([], "RUB")
    assert currency_rub == []


def test_transaction_descriptions() -> None:
    """Тест генератора на корректный вывод названия операций"""
    descriptions = transaction_descriptions(transactions)
    for n in range(1):
        assert next(descriptions) == "Перевод организации"
        assert next(descriptions) == "Перевод со счета на счет"


def test_transaction_descriptions_none() -> None:
    """Тест работы генератора без данных"""
    descriptions = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(descriptions)


def test_card_number_generator():
    """Тест генератора на вывод правильных номеров карт в заданном диапазоне"""
    for card_number in card_number_generator(1, 5):
        assert card_number == str(card_number)
