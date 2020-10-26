import traceback

def incorrect(a, b):
    return a / b

try:
    res = incorrect(5, 0)
except Exception as e:
    print('Ошибка:\n', traceback.format_exc())