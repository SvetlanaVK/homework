n = int(input('enter non-negative whole number: '))

a, b = 1, 1
for i in range(n):
	a, b = b, a + b

print('n-th Fibonacci number: ' + str(a))
