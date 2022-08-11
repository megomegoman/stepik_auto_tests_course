from random import randint
from math import log, ceil

def is_valid(text, predel):
	if text.isdigit() and (0 < int(text) < predel + 1):
		return True
	else:
		return False

yes = "ДА"

while yes == "ДА":
	n = int(input("Введите верхний предел до которого будем загадывать число \n\n"))
	print("Добро пожаловать в числовую угадайку! \n\n Загадано число от 1 до {0}.".format(n))
	print("Попробуйте его отгадать с наименьшим количеством попыток\n")
	num = randint(1, n)
	count = 1
	otvet = input("Введите число от 1 до {0} ".format(n))
	while True:
		if is_valid(otvet, n):
			otvet = int(otvet)
			if otvet > num:
				otvet = input("Загаданное число меньше Вашего, попробуйте еще раз \n")
			elif otvet < num:
				otvet = input("Загаданное число больше Вашего, попробуйте еще раз \n")
			else:
				print("Вы угадали, поздравляем!")
				break
		else:
			otvet = input('А может быть все-таки введем целое число от 1 до {0}? '.format(n))
			continue
		count += 1
	print("Количество попыток: {0}".format(count))
	print("Минимальное кол-во попыток необходимых для 100%-го угадывания: {0} \n".format(ceil(log(n, 2))))
	yes = input("Введите 'ДА' если хотите сыграть еще раз ")
	print("\n"*100)