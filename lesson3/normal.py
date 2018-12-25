# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
	series = []

	a, b = 1, 1
	for i in range(m):
		if i >= n:
			series.append(a)
		a, b = b, a + b

	return series


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def my_sort(elements):
	for i in range(1, len(elements)):
		j = i
		while j > 0 and elements[j-1] > elements[j]:
			elements[j-1], elements[j] = elements[j], elements[j-1]
			j -= 1


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(elements, predicate):
	filtered = []

	for e in elements:
		if predicate(e):
			filtered.append(e)

	return filtered



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# Так не честно, это математика. Я ее люблю, но уже все забыла((

def parallelogram(p1, p2, p3, p4):
	v1 = make_vector(p1, p2)
	v2 = make_vector(p2, p3)
	v3 = make_vector(p4, p3)
	v4 = make_vector(p1, p4)

	return same_vectors(v1, v3) and same_vectors(v2, v4)

def make_vector(begin, end):
	return (end[0] - begin[0], end[1] - begin[1])

def same_vectors (v1, v2):
	return v1[0] == v2[0] and v1[1] == v2[1]
