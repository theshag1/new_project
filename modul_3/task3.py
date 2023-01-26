def get_num(n):
    def num(x):
        count = x + n
        return count * 2

    return num


get_there = get_num(3)
get_two = get_num(2)
get_five = get_num(5)
print(get_five(5))
