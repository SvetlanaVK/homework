n = int(input('enter natural number '))
m = 0
while n > 0:
	(n, d) = divmod(n, 10)
	m = max(m, d)
print('the max digit is ' + str(m))