def mask_account_card(card_info:str) -> str:
    """Маскирует часть номера счета или карты"""
    global get_mask_card_number
    card_number_info: str = ''
    type_info = ''
    for info in card_info:
        if info.isdigit():
            card_number_info += info
        else:
            type_info += info
    card_number_type = ''
    import masks
    if len(card_number_info) <= 16:
        card_number_type = masks.get_mask_card_number(card_number_info)
    else:
        card_number_type = masks.get_mask_account(card_number_info)
    return type_info + card_number_type



def get_date(full_date: str) -> str:
    """ Сокращает запись даты """
    short_date = full_date[8:10] + '.' + full_date[5:7] + '.' + full_date[:4]
    return short_date

print(get_date("2024-03-11T02:26:18.671407"))



