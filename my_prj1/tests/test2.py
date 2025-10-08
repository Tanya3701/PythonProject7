def get_mask_account(account: int) -> str:
    """Маскирует часть банковского счета"""
    account_list = list(str(account))
    account_list[:-4] = "**"
    return "".join(account_list)
print(get_mask_account(73654108430135874305))

