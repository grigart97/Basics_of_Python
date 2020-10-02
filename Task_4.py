input_str = input('Введите предложение и я выведу каждое слово в нём с новой строки и пронумерую каждую строку:')
input_list = input_str.split()
for i, el in enumerate(input_list):
    print(f'{i + 1}-е слово - {el[:10]}')
