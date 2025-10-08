from typing import List

def get_mask_card_number(card_number:int) -> str:
    """Маскирует часть номера карты"""

    card_number_list = list(str(card_number))
    card_number_list[6:12] = '******'
    quarter_one = card_number_list[:4]
    quarter_two = card_number_list[4:8]
    quarter_three = card_number_list[8:12]
    quarter_four = card_number_list[12:16]
    return ''.join(quarter_one) + ' ' + ''.join(quarter_two) + ' ' + ''.join(quarter_three) + ' ' + ''.join(quarter_four)
print(get_mask_card_number(1234567891234567))