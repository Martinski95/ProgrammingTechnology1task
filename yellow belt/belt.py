"""
Условие на задачата:
Да се въведе името на файла от командния ред, в който ще записваме данните.Във наличния файл имаме:
i - ред
x - стойност
Трябва в новия файл да запишем i, x, (i+x)7 и така на всеки ред.
Задачата ми е вярна, моля без повече опити да я разваляте!Ако имате нещо неясно - Мартин Кирилов, можете да ме намерите.
"""

import sys

pathToWrite = sys.argv[1]

csv = open("belt1_1.csv", "r")
i = 0
writeTo = open(pathToWrite, "w")
for line in csv:
	arr = line.split(",")
	y = int((int(arr[0])+int(arr[1]))/7)
	writeTo.write(arr[0] +","+ str(int(arr[1]))+"," + str(y) + ",\n")
	i+= 1