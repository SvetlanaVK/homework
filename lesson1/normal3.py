import math

a = float(input('enter coefficient a: '))
b = float(input('enter coefficient b: '))
c = float(input('enter coefficient c: '))

d = math.sqrt(b**2 - 4 * a * c)

x1 = (-b - d) / (2 * a)
x2 = (-b + d) / (2 * a)

print('x1: ' + str(x1))
print('x2: ' + str(x2))