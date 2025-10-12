def filter_by_state(list_state_info: list, state_info = "EXECUTED") -> list:

    """ Фильтр словарей по статусу """

    new_list_info = []
    for info in list_state_info:
        if info["state"] == state_info:
            new_list_info.append(info)
    return new_list_info
