#from math import abs

def shifr_cesar(text, language, step, shifr):
	text2 = []
	if language == "ru":
		start_A, start_a, count_ru_or_en = 1040, 1072, 32
	elif language == "en":
		start_A, start_a, count_ru_or_en = 65, 97, 26
	if shifr == "-":
		step = count_ru_or_en - step
	
	for	i in text:
		if i.isalpha():
			if i.islower():
				text2 += [(chr((ord(i) - start_a + step) % count_ru_or_en + start_a))]
			else: 
				text2 += [(chr((ord(i) - start_A + step) % count_ru_or_en + start_A))]
		else:
			text2 += [i]
	return "".join(text2)

shifr = input("Будем шифровать(+) или дешифровать(-)?(Введи + или -) ")
while shifr != "+" and shifr != "-":
	 shifr = input("Либо '+'' Либо '-'') ").lower()

lang = input("Какой язык RU  или EN ").lower()
while lang != "ru" and lang != "en":
	lang = input("Либо RU  Либо EN ").lower()

step = int(input("Какой шаг сдвига? ")) 

text = input("Введите текс ")

print(shifr_cesar(text, lang, step, shifr))