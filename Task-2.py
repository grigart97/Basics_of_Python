def params_print(name, fname, dateb, city, email):
    print(f'Итак, Вас зовут {name} {fname} {dateb} '
          f'года рождения из {city}, а Ваш Email: {email}')


input_params = list(map(str, input('Write your name, family name, Date of Birth, city and Email: ').split()))

params_print(name=input_params[0], fname=input_params[1], dateb=input_params[2], city=input_params[3], email=input_params[4])
