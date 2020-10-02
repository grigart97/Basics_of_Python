items_bd = []
close_button = 1
i = 1
while close_button:
    new_item_name = input(f'Введите название {i}-го товара: ')
    new_item_price = float(input(f'Введите цену {i}-го товара: '))
    new_item_quantity = float(input(f'Введите количество {i}-го товара: '))
    new_item_unit = input(f'Введите единицу измерения {i}-го товара: ')
    items_bd.append((i, {'Name': new_item_name, 'Price': new_item_price, 'Quantity': new_item_quantity,
                         'Unit of measure': new_item_unit}))
    i += 1
    close_button = int(input('Будем добавлять новый товар? (1 - да, 0 - нет) '))
for el in items_bd:
    print(el)
transparent_list = []
for i in range(len(items_bd)):
    transparent_list.append(list(items_bd[i][1].values()))
transparent_list = list(zip(*transparent_list))
dict_for_analitics = {'Name': list(transparent_list[0]), 'Price': list(transparent_list[1]),
                      'Quantity': list(transparent_list[2]), 'Unit of measure': list(transparent_list[3])}
print()
print('Итак, аналитика:')
for key in dict_for_analitics:
    print(f'{key}: {dict_for_analitics[key]}')
