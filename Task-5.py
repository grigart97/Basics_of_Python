def sum_elements(list_for_sum):
    """Считает сумму в введенных чисел и общую сумму"""
    global general_sum
    try:
        list_for_sum = list(map(int, list_for_sum))
        general_sum += sum(list_for_sum)
        print(f'Текущая сумма = {sum(list_for_sum)}; Общая сумма = {general_sum}')
    except ValueError:
        print('Введи числа! ')


print('Я буду просить ввести Вас числа разделенные пробелом и буду вычислять их сумму, а также общую сумму')
general_sum = 0
while True:
    input_list = list(input('Введите числа (чтобы выйти, в конце напишите "stop"): ').split())
    if input_list[-1] == 'stop':
        input_list.pop(-1)
        sum_elements(input_list)
        print('Всё!')
        break
    else:
        sum_elements(input_list)
        continue