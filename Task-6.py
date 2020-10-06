def int_func(sentence):
    output_func = []
    for word in sentence:
        word = list(word)
        word[0] = chr(ord(word[0]) - 32)
        output_func.append(''.join(word))
    return output_func


input_sentence = list(input('Введите предложение и я сделаю все слова в нём с большой буквы: \n').split())
output_sentence_1 = int_func(input_sentence)
print('Первый вариант реализации:', end=' ')
for i in output_sentence_1:
    print(f'{i}', end=' ')
print()
print('Второй вариант реализации:', end=' ')
for i in input_sentence:
    print(f'{i.capitalize()}', end=' ')
