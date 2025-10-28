import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions


def test_filter_by_currency(fixture_filter_by_currency_usd) -> None:
    """Тест корректного фильтра транзакции по заданной валюте"""
    assert filter_by_currency(transactions, currency="USD") == fixture_filter_by_currency_usd



def test_filter_by_no_currency(fixture_filter_by_currency_usd):
    """Тест на отсутствие заданной валюты"""
    assert filter_by_currency(fixture_filter_by_currency_usd, currency="RUB") == []


def test_filter_by_not_currency():
    """Тест пустой список"""
    assert filter_by_currency([], currency="RUB") == []








