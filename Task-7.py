import json
import functools


def sum_positive(el_1, el_2):
    if el_1 > 0 and el_2 > 0:
        return el_1 + el_2
    elif el_1 > 0 > el_2:
        return el_1
    elif el_1 < 0 < el_2:
        return el_2


dict_comp = dict()
with open('Task-7_file1.txt', 'r', encoding='utf-8') as tf7_1:
    for raw in tf7_1.readlines():
        dict_comp.update({raw.split()[0]: int(raw.split()[2]) - int(raw.split()[3])})
list_comp = [dict_comp, {'average_profit': functools.reduce(sum_positive, dict_comp.values())}]
print(list_comp)
with open('Task-7_file2.json', 'w', encoding='utf-8') as tf7_2:
    json.dump(list_comp, tf7_2, ensure_ascii=False, indent=4)


