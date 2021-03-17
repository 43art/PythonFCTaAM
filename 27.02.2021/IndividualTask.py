import math

class Quad:
    pos = []

    def __init__(self):
        print("Введите значения координат квадрата (x, y):")
        for i in range(0, 4):
            self.pos.append(int(input()))

    def output(self):
        print(self.pos)

    def square(self):
        return pow((abs(self.pos[0] - self.pos[4]) + abs(self.pos[1] - self.pos[3])), 2)

class Pentagon:
    pos = []

    def __init__(self):
        print("Введите знач")