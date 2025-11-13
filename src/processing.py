def filter_by_state(
        list_state_info: list[dict], state_info: str = "EXECUTED"
) -> list[dict]:
    """Фильтр словарей по статусу"""

    new_list_info = []
    for info in list_state_info:
        if info.get("state") == state_info:
            new_list_info.append(info)
    return new_list_info


def sort_by_date(
        list_state_info: list[dict], sorting_reverse: bool = True
) -> list[dict]:
    """Сортирует по дате (по умолчанию на убывание)"""

    sort_by_date_list = sorted(
        list_state_info, key=lambda info: info.get("date"), reverse=sorting_reverse
    )
    return sort_by_date_list
