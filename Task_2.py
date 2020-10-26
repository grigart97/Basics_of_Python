input_str = input('Введите список элементов списка через пробел и я поменяю местами каждые два соседних элемента: ')
input_list = list(input_str.split())
for i in range(1, len(input_list) - len(input_list) % 2, 2):
    input_list[i], input_list[i - 1] = input_list[i - 1], input_list[i]
print(input_list)
