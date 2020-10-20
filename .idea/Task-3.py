class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return Cell(self.quantity - other.quantity) if self.quantity - other.quantity > 0 else  0

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __floordiv__(self, other):
        return Cell(self.quantity // other.quantity)

    def __str__(self):
        return f'{self.quantity}'

    def make_order(self, q_inline):
        my_list = list('*' * self.quantity)
        for i in range(q_inline, self.quantity, q_inline+1):
            my_list.insert(i, '\n')
        return ''.join(my_list)
        # q_all = self.quantity
        # for raws in range(q_all // q_inline + 1):
        #     if q_all // q_inline != 0:
        #         for _ in range(q_inline):
        #             print('*', end='')
        #         print()
        #     else:
        #         for _ in range(q_all % q_inline):
        #             print('*', end='')
        #         print()
        #     q_all -= q_inline


a = Cell(14)
b = Cell(8)
print(a+b)
print(a-b)
print(a*b)
print(a//b)

print(a.make_order(5))
