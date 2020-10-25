import functools


def sum_two_el(el_1, el_2):
    return el_1 + el_2


input_list = [el for el in range(100, 1001) if el % 2 == 0]
print(functools.reduce(sum_two_el, input_list))
# print(input_list)
