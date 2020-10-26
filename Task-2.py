input_sec = int(input('Поехали! Сейчас я превращу секунды в часы и минуты! Введите любое целое число секунд: '))
hours = input_sec // 3600
minutes = input_sec % 3600 // 60
sec = input_sec % 60
print(f'Итого, получилось {hours}:{minutes}:{sec}')