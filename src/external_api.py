import os

import requests
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert"

header = {'apikey': API_KEY}


def currency_conversion(operations: list[dict]) -> str:
    """Выводит сумму оборота транзакции, в случае, транзакции в евро и долларах, конвертирует результат в рубли"""
    for operation in operations:
        transaction_amount = operation.get("operationAmount").get("amount")
        if operation.get("operationAmount").get("currency").get("code") == "RUB":
            return transaction_amount
        elif operation.get("operationAmount").get("currency").get("code") == "USD":
            payload = {"amount": transaction_amount, "from": "USD", "to": "RUB"}
            response = requests.get(url, headers=API_KEY, params=payload)
            return round(response.json()["result"], 2)
        elif operation.get("operationAmount").get("currency").get("code") == "EUR":
            payload = {"amount": transaction_amount, "from": "EUR", "to": "RUB"}
            response = requests.get(url, headers=header, params=payload)
            return round(response.json()['result'], 2)
