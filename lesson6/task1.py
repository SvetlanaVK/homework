# Задача-1:
#
# Создать класс треугольник и реализовать в нем конструктор, методы для вычисления (не печати, нужен return) площади,
# периметра и вывод значений сторон треугольника на экран. В конструкторе сделать проверку на возможность создания такого 
# треугольника, если нет, то написать, что такой треугольник нельзя создать и сделать exit(1)


import sys
import math

class Triangle:
    def __init__(self, a, b, c):
        Triangle._validate_sides(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return a + b + c

    def get_area(self):
        s = (self.a + self.b + self.c) * (self.a + self.b) \
            * (self.a + self.c) * (self.b + self.c) / 16
        return math.sqrt(s)

    def _validate_sides(a, b, c):
        if a + b < c or a + c < b or b + c < a:
            print('Invalid sides. a = {}, b = {}, c = {}'.format(a, b, c))
            sys.exit(1)

