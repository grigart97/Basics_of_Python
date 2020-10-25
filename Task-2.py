import random as rnd

num_list = [rnd.randint(0, 50) for _ in range(10)]
result_list = [el for i, el in enumerate(num_list) if el > num_list[i - 1] and i != 0]
print(f'Исходный список: {num_list}\nРезультирующий список: {result_list}')

# Помощь Сереже
# orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
