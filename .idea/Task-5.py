""" Реализовал задачу двумя вариантами:
1. Как требуется в задаче (закомментированные строки в каждом дочернем классе.
2. Как считаю, более логичным, элегантным и т.д. и т.п.
В каждом дочернем классе закомментировал """

class Stationery:
    title = 'item'
    def draw(self):
        print(f'Start to paint with your {self.title}')

class Pen(Stationery):
    title = 'pen'
    #def draw(self):
    #    print(f'Lets draw with {self.title}')

class Pencil(Stationery):
    title = 'pencil'
    #def draw(self):
    #    print(f'I wanna with {self.title}')

class Handle(Stationery):
    title = 'handle'
    #def draw(self):
    #    print(f'I want you to draw with {self.title}')

# test Stationery
test = Stationery()
test.draw()
print()
# test Pencil
a = Pencil()
a.draw()
print()
# test Pen
b = Pen()
b.draw()
print()
# test Handle
c = Handle()
c.draw()