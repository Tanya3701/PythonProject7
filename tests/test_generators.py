import pytest

from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
    transactions,
)


def test_filter_by_currency(fixture_filter_by_currency_usd) -> None:
    """Тест корректного фильтра транзакции по заданной валюте"""
    assert (
        filter_by_currency(transactions, currency="USD")
        == fixture_filter_by_currency_usd
    )


def test_filter_by_no_currency(fixture_filter_by_currency_usd):
    """Тест на отсутствие заданной валюты"""
    assert filter_by_currency(fixture_filter_by_currency_usd, currency="RUB") == []


def test_filter_by_not_currency():
    """Тест пустой список"""
    assert filter_by_currency([], currency="RUB") == []


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
