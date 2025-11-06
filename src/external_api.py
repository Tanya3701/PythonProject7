from src.utils import *
import json
import requests

API_KEY = {"apikey": "3cCuvPm5Ze427naeRFAimu05zK1IOZqd"}
url = 'https://api.apilayer.com/exchangerates_data/convert'


def currency_conversion(operations: list[dict]) -> None:
    for operation in operations:
        transaction_amount = operation.get("operationAmount").get("amount")
        if operation.get("operationAmount").get("currency").get("code") == 'RUB':
            return transaction_amount
        elif operation.get("operationAmount").get("currency").get("code") == 'USD':
            payload = {"amount": transaction_amount,
                       "from": "USD",
                       "to": "RUB"
                       }
            response = requests.get(url, headers=API_KEY, params=payload)
            return response.json()['query']['amount']
        elif operation.get("operationAmount").get("currency").get("code") == 'EUR':
            payload = {"amount": transaction_amount,
                       "from": "EUR",
                       "to": "RUB"
                       }
            response = requests.get(url, headers=API_KEY, params=payload)
            return round(response.json()['result'], 2)
