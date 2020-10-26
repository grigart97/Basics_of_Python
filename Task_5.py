my_list = [7, 5, 3, 3, 2]
close_button = 1
while close_button:
    new_rating = int(input('Введите новый элемент рейтинга и я поставлю его в нужное место: '))
    if my_list.count(new_rating) > 0:
        for ind, el in enumerate(my_list):
            if el == new_rating:
                insert_index = ind
        my_list.insert(insert_index + 1, new_rating)
    else:
        my_list.append(new_rating)
    print(f'Итак, вот что получилось: {my_list}')
    close_button = int(input('Есть ли ещё элмементы рейтинга? (1 - да; 0 - нет): '))

