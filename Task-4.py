import random as rnd
# input_list = [rnd.randint(0, 45) for _ in range(15)] Учусь рандому
input_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Исходный список: {input_list}\nСписок его элементов, не имеющие повторений: {[el for el in input_list if input_list.count(el) == 1]}')
