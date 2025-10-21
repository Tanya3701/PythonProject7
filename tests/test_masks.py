import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    {
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
    },
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected
    """Тестирование правильности маскирования номера карты"""


def test_get_mask_card_number_invalid_card_number() -> None:
    """Тестирование исключений"""
    with pytest.raises(ValueError):
        get_mask_card_number("")
        get_mask_card_number("68319824767376589")


@pytest.mark.parametrize(
    "account, expected",
    {
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    },
)
def test_get_mask_account(account: str, expected: str) -> None:
    assert get_mask_account(account) == expected


def test_get_mask_invalid_account() -> None:
    with pytest.raises(ValueError):
        get_mask_account("")
        get_mask_account("73654108430135874305")
        get_mask_account("3538303")

