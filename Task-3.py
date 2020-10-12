with open('Task-3_file.txt', 'a+', encoding='utf-8') as tf3:
    while True:
        raw = input('Построчно введите фамилии сотрудников и их оклад: (чтобы закончить введите пустую строку)\n')
        if len(raw.split()) == 2 and raw[1].isdigit():
            print(raw, file=tf3)
        elif raw =='':
            break
        else:
            print('Ты неправильно вводишь параметры... Попробуй ещё раз')
            continue
    tf3.seek(0)
    men_salaries = dict()
    for raw in tf3.readlines():
        men_salaries.update({raw.split()[0]: int(raw.split()[1])})
    print('Сотрудники с зарплатой менее 20 000:')
    print({fname: men_salaries[fname] for fname in men_salaries if men_salaries[fname] < 20000})
    print(f'Среднее значение оклада: {sum(men_salaries.values()) / len(men_salaries):.3f}')
