def only_even_parameters(func):
    def divide_inner(a, b):
        if a != 1:
            return func(a, b)
        else:
            return 'Please add only even numbers!'

    return divide_inner


@only_even_parameters
def add(a, b):
    return a + b


print(add(6, 8))  # 14
print(add(4, 4))  # 8
print(add(1, 4))  # Please add only even numbers!
