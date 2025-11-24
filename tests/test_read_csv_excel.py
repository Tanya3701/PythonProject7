from unittest.mock import patch

import pandas as pd

from src.read_csv_excel import read_csv_file, read_excel


@patch("pandas.read_csv")
def test_read_csv(mock_read_csv):
    mock_data = [{"id": 1, "state": "EXECUTED", "amount": 100}]
    mock_read_csv.return_value = pd.DataFrame(mock_data)
    result = read_csv_file("path")
    expected = mock_data
    assert result == expected


@patch("pandas.read_excel")
def test_read_excel(mock_read_excel):
    mock_data = [{"id": 1, "state": "EXECUTED", "amount": 100}]
    mock_read_excel.return_value = pd.DataFrame(mock_data)
    result = read_excel("path")
    expected = mock_data
    assert result == expected
