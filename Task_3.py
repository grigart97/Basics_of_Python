yes_button = 1
while yes_button:
    months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
    num_month = int(input('Введите номер месяца, и я скажу, какое это время года: '))
    if num_month <= 12:
        print(f'Эх, {months[num_month - 1]}! Приятная пора!')
    else:
        yes_button = int(input(f'Кажется, месяца под номером {num_month} не существует... Попробуем ещё раз? (1 - да, 0 - нет) '))