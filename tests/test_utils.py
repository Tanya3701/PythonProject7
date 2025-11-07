from src.utils import json_read_file
from unittest.mock import mock_open
from unittest.mock import patch



@patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
@patch('os.path.exists')
@patch('os.path.getsize')
def test_load_operations_returns_dict(mock_getsize, mock_exists, mock_open):
    mock_exists.return_value = True
    mock_getsize.return_value = 1
    result = json_read_file('test_file.json')
    assert isinstance(result, dict)