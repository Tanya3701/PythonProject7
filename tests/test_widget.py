import pytest

from widget import mask_account_card, get_date


@pytest.mark.parametrize("card_info, expected", [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                                 ('Счет 64686473678894779589', 'Счет **9589'),
                                                 ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                                                 ('Счет 35383033474447895560', 'Счет **5560' ),
                                                 ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                                 ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
                                                 ('Visa Gold 7158300734726758', 'Visa Gold 7158 30** **** 6758'),
                                                 ('Счет 71583007347267589874', 'Счет **9874')])

def test_mask_account_card(card_info, expected):
    """Проверка, что функция корректно распознает и
    применяет нужный тип маскировки в зависимости от
    типа входных данных (карта или счет)."""
    assert mask_account_card(card_info) == expected

def test_mask_invalid_account_card():
    """проверка исключений"""
    with pytest.raises(ValueError):
        mask_account_card("")
        mask_account_card("1234")
        mask_account_card("123456789123456789123456789123456")





