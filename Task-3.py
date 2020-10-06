def my_func(num_1, num_2, num_3):
    return sum([num_1, num_2, num_3]) - min([num_1, num_2, num_3])


try:
    [a, b, c] = list(map(int, input('Введите три числа через пробел и я посчитаю сумму двух наибольших: ').split()))
    print(my_func(a, b, c))
except ValueError:
    print('Я же просил ввести числа!')
