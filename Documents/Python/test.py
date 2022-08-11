from random import *
a = ["Рыков", "Шилов", "Пикалов", "Черемахин", "Лёзова", "Мареев"]
shuffle(a)
b = [randrange(len(a)) for _ in range(10000)]
for i in range(len(a)):
	print("{0} выпал {1} раз(а)".format(a[i], b.count(i))) 
