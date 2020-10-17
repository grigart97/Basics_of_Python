class Road:
    mass_asp_cm = 25
    cm = 5

    def __init__(self, length, width):
        self._length = length
        self._wigth = width

    def count_mass_asphalt(self):
        print(f'Необходимо {(self._length * self._wigth * self.mass_asp_cm * self.cm) / 1000} т.')

A16 = Road(5000, 20)
A16.count_mass_asphalt()