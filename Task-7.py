import functools as ft


def fact(n):
    fact_n = 1
    for i in range(1, n + 1):
        fact_n *= i
        yield i, fact_n


input_n = int(input('Введите число, факториал которого необходимо вычислить: '))
print(f'{input_n}! = ', end='')
for el in fact(input_n):
    if el[0] == 1:
        print(f'{el[0]}', end=' ')
    else:
        print(f'* {el[0]}', end=' ')
print(f'= {el[1]}')

