def get_mask_card_number(card_number: str) -> str:
    """Маскирует часть номера карты"""

    if len(card_number) != 16:
        raise ValueError("Неверный номер карты")
    else:
        card_number_list = list(card_number)
        card_number_list[6:12] = "******"
        quarter_one = card_number_list[:4]
        quarter_two = card_number_list[4:8]
        quarter_three = card_number_list[8:12]
        quarter_four = card_number_list[12:16]
        return (
                "".join(quarter_one)
                + " "
                + "".join(quarter_two)
                + " "
                + "".join(quarter_three)
                + " "
                + "".join(quarter_four)
        )


def get_mask_account(account: str) -> str:
    """Маскирует часть банковского счета"""
    if len(account) != 20:
        raise ValueError("Неверный счет")
    else:
        account_list = list(account)
        account_list[:-4] = "**"
        return "".join(account_list)
