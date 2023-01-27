def add_func(func):
    def add_result_func(number, number_2):
        return (number + number_2) * 2

    return add_result_func


@add_func
def target(number, number_2):
    return number + number_2


result = target(2, 3)
print(result)