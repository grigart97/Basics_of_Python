def my_func1(x, y):
    """Возводит число x в степень -y через цикл"""
    result = 1
    y = abs(y)
    for i in range(y):
        result *= x
    return round(1 / result, 3)


def my_func2(x, y):
    """Возводит число x в степень -y через оператор **"""
    y = abs(y)
    return round(x ** -y, 3)



try:
    base_degree = float(input('Введите основание степени: '))
    power_degree = int(input('Введите степень, в которую возвести '
                             '(отрицательную. Если она будет положительная, я поменяю знак): '))
    print(my_func1(base_degree, power_degree))
    print(my_func2(base_degree, power_degree))
except ValueError:
    print('Я же просил ввести число!')