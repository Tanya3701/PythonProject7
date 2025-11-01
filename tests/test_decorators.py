import pytest
from src.decorators import log, my_function



def test_log(capsys):
    my_function(1, 0)
    captured = capsys.readouterr()
    assert captured.out == 'my_function error: division by zero Inputs: (1, 0) {}\n'

def test_log(capsys):
    my_function(1, 1)
    captured = capsys.readouterr()
    assert captured.out == 'my_function: ok Вывод: 1.0\n'