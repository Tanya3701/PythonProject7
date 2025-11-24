import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import currency_conversion

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")
header = {"apikey": API_KEY}


@patch("requests.get")
def test_currency_conversion(mock_get):
    mock_get.return_value.json.return_value = {"result": 50}
    assert (
        currency_conversion(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {"name": "USD", "code": "USD"},
                },
            }
        )
        == 50.00
    )
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers=header,
        params={"amount": "8221.37", "from": "USD", "to": "RUB"},
    )
