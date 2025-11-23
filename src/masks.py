import logging

logger = logging.getLogger("masks.py")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    filename=r"logs\masks.log", encoding="utf-8", mode="w"
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует часть номера карты"""

    if len(card_number) != 16:
        logger.error("Неверный номер карты")
        return None
    else:
        card_number_list = list(card_number)
        card_number_list[6:12] = "******"
        quarter_one = card_number_list[:4]
        quarter_two = card_number_list[4:8]
        quarter_three = card_number_list[8:12]
        quarter_four = card_number_list[12:16]
        logger.info("Успешная маскировка")
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
        logger.error("Неверный номер счета")
        return None
    else:
        account_list = list(account)
        account_list[:-4] = "**"
        logger.info("Успешная маскировка")
        return "".join(account_list)
