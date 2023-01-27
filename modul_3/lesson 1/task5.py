def get_lst(func):
    def lst_get(lst):
        if type(lst) == list:
            return sum([i for i in range(len(lst))])
        else:
            print('input only lst ! ')

    return lst_get


@get_lst
def get_sum(lst):
    return lst


lst = [2, 3, 4, 5]
tpl = (1 , 2,3,5)
print(get_sum(lst))
# print(get_sum(tpl))
