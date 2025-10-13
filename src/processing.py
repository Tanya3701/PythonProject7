def filter_by_state(list_state_info: list, state_info: str = "EXECUTED") -> list:

    """ Фильтр словарей по статусу """

    new_list_info = []
    for info in list_state_info:
        if info["state"] == state_info:
            new_list_info.append(info)
    return new_list_info


def sort_by_date(list_state_info: list, sorting_reverse: bool = True) -> list:

    """ Сортирует по дате (по умолчанию на убывание)"""

    sort_by_date_list = sorted(list_state_info, key=lambda info: info["date"], reverse=sorting_reverse)
    return sort_by_date_list
