import traceback


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_1, num_2 = input('Введите числа через пробел и я их поделю (сначала делимое, потом делитель)\n').split()
try:
    int(num_1)

    if int(num_2) == 0:
        raise OwnError('Ну и зачем ты пытаешь поделить на ноль!? Я отказываюсь с тобой работать!')
except ValueError:
    print('Ошибка!\n', traceback.format_exc())
except OwnError as err:
    print(err)
else:
    print(f'А вот и результат: {int(num_1) / int(num_2):.3f}')