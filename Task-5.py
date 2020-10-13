with open('Task-5_file.txt', 'w+', encoding='utf-8') as tf5:
    print('Сейчас я посчитаю сумму вводимых Вами чисел!')
    while True:
        raw = input('Построчно введите числа: (чтобы закончить введите пустую строку)\n')
        if raw.isdigit():
            print(raw, file=tf5)
        elif raw == '':
            break
        else:
            print('Ты неправильно вводишь параметры... Попробуй ещё раз')
            continue
    tf5.seek(0)
    dig_sum = 0
    for raw in tf5.readlines():
        dig_sum +=int(raw[0:-1])
    print(f'Сумма чисел: {dig_sum}')