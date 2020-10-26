my_list = [[None, True], (2, 3.0), ({'four', b'five'}), {6 + 7j: "восемь"}]
print(f'{my_list} - это {type(my_list)}, в котором:')
for i in my_list:
    in_my_list = i
    print(f'{type(in_my_list)}, в котором:', end=' ')
    for j in in_my_list:
        print(type(j), end=' ')
    print()
