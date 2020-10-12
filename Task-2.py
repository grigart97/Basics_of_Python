with open('Task-2_file.txt', 'r', encoding='utf-8') as tf:
    for i, raw in enumerate(tf.readlines()):
        print(f'{i + 1}-ая строка - "{raw[0:-1]}" содержит {len(raw) - 1} символов')
    print(f'Всего в файле {i + 1} строк')
