class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def numbers(cls, date):
        nums = {'day': int(date.split('-')[0]), 'month': int(date.split('-')[1]), 'year': int(date.split('-')[2])}
        return nums

    @staticmethod
    def validate(date):
        if date['month'] in [1, 3, 5, 7, 8, 9, 10, 12] or date['day'] > 31:
            date['day'] = 31
        elif date['month'] in [4, 6, 9, 11] and date['day'] > 30:
            print('В указанном Вами месяце - 30 дней!')
            date['day'] = 30
        elif date['month'] == 2:
            if date['year'] % 4 != 0 and date['day'] > 28:
                date['day'] = 28
            elif date['day'] > 29:
                date['day'] = 29
        elif date['month'] > 12:
            print('Вы ввели странный номер месяца... Давайте договоримся, что Вы имели в виду число 12!')
            date['month'] = 12
        elif date['month'] < 1:
            return f'Вы указали дату, в котором номер месяца указан неверно.'
        return f'{date["day"]:0=2d}-{date["month"]:0=2d}-{date["year"]:4d}'


a = Date(input('Введите дату в формате дд-мм-ггг: '))
print(a.validate(a.numbers(a.date)))
