with open('text_test.txt', 'w', encoding='utf-8') as test_file:
    while True:
        if i := input('Построчно вводите данные, если хотите закончить, введите пустую строку: \n'):
            print(i, file=test_file)
        else:
            break
