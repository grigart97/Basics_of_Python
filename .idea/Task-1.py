import time
from itertools import cycle


class Trafficlight:
    __color = ['red', 'yellow', 'green', 'yellow']

    def running(self):
        for el in cycle(self.__color):
            print(el)
            time.sleep(7.0 if el == 'red' or el == 'green' else 2.0)


one = Trafficlight()
one.running()