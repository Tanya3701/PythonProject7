import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_info, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 7158300734726758", "Visa Gold 7158 30** **** 6758"),
        ("Счет 71583007347267589874", "Счет **9874"),
    ],
)
def test_mask_account_card(card_info: str, expected: str) -> None:
    """Проверка, что функция корректно распознает и
    применяет нужный тип маскировки в зависимости от
    типа входных данных (карта или счет)."""
    assert mask_account_card(card_info) == expected


def test_mask_invalid_account_card() -> None:
    """проверка исключений"""
    assert mask_account_card("") == " - не определен"
    assert mask_account_card("1234") == " - не определен"
    assert mask_account_card("123456789123456789123456789123456") == " - не определен"


@pytest.mark.parametrize(
    "full_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-12-05T02:26:18.671407", "05.12.2025"),
        ("2025-04-01", "01.04.2025"),
    ],
)
def test_get_date(full_date: str, expected: str) -> None:
    assert get_date(full_date) == expected
