from abc import ABC, abstractmethod

class Clothes (ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def tissue_consumption(self):
        pass

class Coat(Clothes):
    max_size = 66
    min_size = 40

    @property
    def tissue_consumption(self):
        if self.size < self.min_size:
            nat_size = self.min_size
        elif self.size > self.max_size:
            nat_size = self.max_size
        else:
            nat_size = self.size + 1 if self.size % 2 == 1 else self.size
        print(f'Для пальто размером {self.size} необходимо {nat_size / 6.5 + 0.5:.3f} метров ткани')

class Suit(Clothes):
    max_size = 210
    min_size = 120

    @property
    def tissue_consumption(self):
        if self.size < self.min_size:
            nat_size = self.min_size
        elif self.size > self.max_size:
            nat_size = self.max_size
        else:
            nat_size = self.size + 1 if self.size % 2 == 1 else self.size
        print(f'Для костюма размером {self.size} необходимо {nat_size * 2 + 0.3:.1f} метров ткани')

a = Suit(100)
b = Coat(35)
a.tissue_consumption
b.tissue_consumption