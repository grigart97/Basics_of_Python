"""Решил пойти дальше и реализовал код немного логичнее (надеюсь).
Скорость задаются в методе "go", а не при инициализации объекта.
Соответственно, в методе "show_speed" пропала нужда и его функционал добавил в "go".
Так как у "TownCar" и "WorkCar" одинаковые, создал дополнительный родительский класс для них.
Понимаю, что для данной задачи - это ненужно и скорее излишне, но хотя бы разобрался)"""

class Car:

    def __init__(self, color, name, is_police=False):
        self.color, self.name, self.is_police = color, name, is_police
    def go(self, speed):
        print(f'Поехали! Можешь гнать на своей {self.name} со скоростью {speed}!')
    def stop(self):
        print(f'Остановите свой {self.name}! Вите надо выйти!')
    def turn(self, direction):
        print(f'Командир, здесь {direction}')

class Car_with_max_speed(Car):
    def go(self, speed):
        print(f'Поехали! Можешь гнать на своей {self.name} со скоростью {speed}! Придётся превысить, командир!') \
            if speed > self.max_speed else None

class TownCar(Car_with_max_speed):
    max_speed = 60

class SportCar(Car):
    pass

class WorkCar(Car_with_max_speed):
    max_speed = 40

class PoliceCar(Car):
    def __init__(self, color, name, is_police=True):
        super().__init__(color, name, is_police)


# test TwonCar
town = TownCar('green', 'Lada')
town.go(70)
town.turn('направо')
town.stop()
print()
# test SportCar
sport = SportCar('black', 'Lexus')
sport.go(110)
sport.turn('налево')
sport.stop()
print()
# test WorkCar
work = WorkCar('white', 'Ford')
work.go(60)
work.turn('обратно')
work.stop()
print()
# test PoliceCar
police = PoliceCar('blue', 'Ferrari')
police.go(80)
police.turn('в тюрьму')
police.stop()
# test is_police
print(police.is_police)
print(work.is_police)