import pytest

@pytest.fixture
def fixture_card_numbers():
    return [
        ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
        ('Счет 64686473678894779589', 'Счет **9589'),
        ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
        ('Счет 35383033474447895560', 'Счет **5560'),
        ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
        ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
        ('Visa Gold 7158300734726758', 'Visa Gold 7158 30** **** 6758'),
        ('Счет 71583007347267589874', 'Счет **9874')]