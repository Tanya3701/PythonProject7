def filter_by_currency(transactions, currency):
    """Функция фильтра данных по видам валюты"""
    code_list = []
    for transaction in transactions:
        key_operation = transaction.get("operationAmount").get("currency").get("code")
        if key_operation == currency:
            code_list.append(transaction)
    return code_list
