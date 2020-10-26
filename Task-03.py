class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


print('Построчно вводите по одному числу и я соберу из них список. Чтобы закончить ввод - "stop"')
my_list = []
while True:
    num = input()
    if num != 'stop':
        try:
            if not num.isdigit():
                raise OwnError('Я же просил вводить числа! Давай ещё раз!')
        except OwnError as err:
            print(err)
        else:
            my_list.append(int(num))
    else:
        break
print(my_list)