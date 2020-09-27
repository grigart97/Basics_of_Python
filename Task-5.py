revenue = float(input('Введите выручку фирмы: '))
expenses = float(input('Ого! Неплохие показатели! А какова сумма издержек? '))
if revenue > expenses:
    print(f'Поздравляю с прибылью! Рентбельность выручки составила - {revenue/expenses:.3f}')
    employees = int(input('А сколько у Вас работников? '))
    print('Прибыль на одного работника составляет - {:.3f}'.format((revenue-expenses)/employees))
elif revenue < expenses:
    print('Кажется, у Вас убыток...')