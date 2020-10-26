class ComplexNum:
    def __init__(self, num, num_j=0):
        self.num = int(num)
        self.num_j = int(num_j)

    def __add__(self, other):
        return complex(self.num + other.num, self.num_j + other.num_j)

    def __mul__(self, other):
        return complex(self.num * other.num - self.num_j * other.num_j, self.num * other.num_j + self.num_j * other.num)


a = ComplexNum(*input('Введите элементы комлекстного числа через пробел: ').split())
b = ComplexNum(*input('Введите элементы комлекстного числа через пробел: ').split())
print(a+b)
print(a*b)

print(complex(3, 4) * complex(1, 2))