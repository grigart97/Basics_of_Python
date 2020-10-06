def divisin_two_numbers(devinded, divisor):
    """Деление первого числа на второе"""
    try:
        return devinded / divisor
    except ZeroDivisionError:
        return 'Кажется, Вы хотите делить на ноль... Это всегда бесконечность. Пора уж это знать!'

try:
    print(divisin_two_numbers(float(input('Давай делить два числа! Введи делимое: ')),
                          float(input('Отлично! Теперь делитель: '))))
except ValueError:
    print('Кажется, ты пытаешься делить не числа...')