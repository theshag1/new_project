def func_way(func):
    def get_number(num, num2):
        return (num + num2) * 2

    return get_number


@func_way
def target(num, num2):
    return num + num2


result = target(4, 5)
print(result)
