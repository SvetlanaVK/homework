# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

for i in range(1, 10):
	dir = os.path.join(os.getcwd(), 'dir_' + str(i))
	try:
		os.mkdir(dir)
	except FileExistsError:
		print('Directory "{}" already exists.'.format(dir))


