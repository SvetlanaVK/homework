# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

for file in os.listdir(os.getcwd()):
	if os.path.isdir(file):
		print(file)