def get_next_multiple(num):
    count = num
    while True:
        yield num
        num *= count


number = get_next_multiple(2)
iterator = iter(number)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
