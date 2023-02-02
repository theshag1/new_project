def get_sum(funk):
    def sum_get(lst):
        if type(lst) == list:
            return funk(lst)
        else:
            print('input only lst !')

    return sum_get


@get_sum
def all_get(lst):
    return sum((i for i in range(len(lst))))


lst = [1, 2, 4, 4, 5]
print(all_get(lst))
