from unittest.mock import patch

from src.external_api import currency_conversion


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
        headers=None,
        params={"amount": "8221.37", "from": "USD", "to": "RUB"},
    )
