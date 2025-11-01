from src.decorators import log


@log()
def my_function(x: int, y: int) -> float:
    return x / y


def test_log(capsys):
    """Проверка декоратора при неправильной работе функции"""
    my_function(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: division by zero Inputs: (1, 0) {}\n"


def test_log_(capsys):
    """Проверка декоратора при нормальной работе функции"""
    my_function(1, 1)
    captured = capsys.readouterr()
    assert captured.out == "my_function: ok Вывод: 1.0\n"
