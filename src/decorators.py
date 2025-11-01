def log(filename=None):
    def decorator(function):
        def wrapper(*args, **kwargs):
            function_name = function.__name__
            try:
                result = function(*args, **kwargs)
                if filename:
                    file = open(filename, 'a', encoding='utf-8')
                    file.write(f'{function_name}:ok Вывод: {result}' + '\n')
                    file.close()
                else:
                    print(f'{function_name}: ok Вывод: {result}')
            except Exception as e:
                if filename:
                    file = open(filename, 'a', encoding='utf-8')
                    file.write(f'{function_name} error: {e} Inputs: {args} {kwargs}' + '\n')
                    file.close()
                else:
                    print(f'{function.__name__} error: {e} Inputs: {args} {kwargs}')
        return wrapper
    return decorator


@log()
def my_function(x, y):
    return x / y

print(my_function(1, 1))


