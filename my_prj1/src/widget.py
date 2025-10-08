def mask_account_card(card_info: str) -> str:
    """Маскирует часть номера счета или карты"""
    card_number_info: str = ""
    type_info = ""
    for info in card_info:
        if info.isdigit():
            card_number_info += info
        else:
            type_info += info
    card_number_type = ""
    from masks import get_mask_card_number, get_mask_account

    if len(card_number_info) <= 16:
        card_number_type = get_mask_card_number(card_number_info)
    else:
        card_number_type = get_mask_account(card_number_info)
    return type_info + card_number_type


def get_date(full_date: str) -> str:
    """Сокращает запись даты"""
    short_date = full_date[8:10] + "." + full_date[5:7] + "." + full_date[:4]
    return short_date
