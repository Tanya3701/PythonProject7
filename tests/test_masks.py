import pytest

from src.masks import *


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


def test_get_mask_card_number_invalid_card_number() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("")
        get_mask_card_number("68319824767376589")
