dict_en_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('Task-4_file1.txt', 'r', encoding='utf-8') as tf4_1:
    a = tf4_1.readlines()
    print(a)
list_to_insert = []
for i in a:
    raw = i.split()
    raw[0] = dict_en_rus.get(raw[0])
    raw = ' '.join(raw)
    list_to_insert.append(raw)
with open('Task-4_file2.txt', 'w', encoding='utf-8') as tf4_2:
    for raw in list_to_insert:
        print(raw, file=tf4_2)
