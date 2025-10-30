import pytest

from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
    transactions,
)


def test_filter_by_currency() -> None:
    """Тест корректного фильтра транзакции по заданной валюте"""
    currency_usd = filter_by_currency(transactions, "USD")
    for currency in range(1):
        assert next(currency_usd) == {
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
        }


def test_filter_by_no_currency(fixture_filter_by_currency_usd):
    """Тест на отсутствие заданной валюты"""
    currency_rub = filter_by_currency(fixture_filter_by_currency_usd, "RUB")
    for currency in range(1):
        with pytest.raises(StopIteration):
            next(currency_rub)


def test_filter_by_not_currency():
    """Тест пустой список"""
    currency_rub = filter_by_currency([], "RUB")
    for currency in range(1):
        with pytest.raises(StopIteration):
            next(currency_rub)


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
