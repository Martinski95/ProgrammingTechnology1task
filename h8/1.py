"""Технологично училище „Електронни системи” http://www.elsys-bg.org/
11 А
17
Мартин Красимиров Кирилов
Трябва да се открие
a. Кой е най-свързаният номер в клас - всеки ученик получава листа от друг. Написва си номера на него. Човекът, който е получил лист най-много пъти е най-свързаният номер в клас
b. Кой е най-малко свързаният номер в клас - аналогично на горната, човекът написал най-малко пъти номера си е най-малко свързаният.
c. За всеки номер да се намери на кой номер е предал листа най-много пъти - ако на даден лист поредния номер е 4, а следващият е 7 то номер 4 е предал листа на номер 7. Номер 4 е предал листа и на много други номера. Да се намери кой е номерът на който номер 4 е предал листа най-много пъти. Аналогично да се намери и за останалите номера.
d. За всеки номер да се намери кой номер му е предал листа най-много пъти - ако на даден лист поредния номер е 4, а следващият е 7 то номер 4 е предал листа на номер 7. Номер 7 е получил листа и от много други номера. Да се намери кой е номерът, който най-много пъти е дал листа на номер 7. Аналогично да се намери за всеки един номер.
e. За точки c и d да се намерят стойностите на най-малко предадените и получените листове.
"""

import os

arr = []
data = [[0]*31 for x in range(31)]

for i in range(30):
	arr.append(0)

for i in range(1,29):
	csv = open(str(i) + ".csv")
	temp = 0
	for line in csv:
		x = line.split(",")
		arr[int(x[1])] += 1
		data[i][int(x[0])] = int(x[1])

def drawMenu():
	print("Press 1 to get the most popular person in class.")
	print("Press 2 to get the least popular person in class.")
	print("Press 3 to get the most sent list in class.")
	print("Press 4 to get the most received list in class.")
	print("Press 5 to get the least sent list in class.")
	print("Press 6 to get the least received list in class.")
	print("Press 7 to exit.")
	s = input(': ')
	return int(s)
		
def mostPopular():
	maxID = 0
	maxx = 0
	for i in range(1,29):
		if arr[i] > maxx:
			maxID = i
			maxx = arr[i]
	print("Most popular person is ", maxID, " with ", maxx, " votes.")
	
def leastPopular():
	minID = 0
	minn = 1000
	for i in range(1, 29):
		if arr[i] < minn:
			minID = i
			minn = arr[i]
	print("Least popular person is ", minID, " with ", minn, " votes")

def mostSend(x, cast): 	
		#case is the managing variable on which you decice what to do
		#x is the sender number
	maxSend = []
	for i in range(30):
		maxSend.append(0)
	for i in range(1,29):
		for j in range(1,30):
			if data[i][j] == x:
				maxSend[data[i][j+1]] += 1
	maxnum = 0
	minnum = 0
	for i in range(0,30):
		if maxSend[i] == max(maxSend):
			maxnum = i
		if maxSend[i] == min(maxSend):
			minnum = i
	if cast == 1:
		if max(maxSend) < 1:
			print("Nomer", x, "ne predal na nikogo!!!")
		else:
			print("Nomer", x, "e predal nai-mnogo(",max(maxSend),")puti na nomer", maxnum)
	elif cast == 5:
		print("Nomer", x, "e predal nai-malko(",min(maxSend),")puti na nomer", minnum)
	

def mostReceived(x, cast): 
		#case is the managing variable on which you decice what to do
		#x is the receiver number
	maxReceived = []
	for i in range(30):
		maxReceived.append(0)
	for i in range(1,29):
		for j in range(1,30):
			if data[i][j] == x:
				if j == 1:
					maxReceived[data[i][j]] += 1
				else:
					maxReceived[data[i][j-1]] += 1
	maxnum = 0
	minnum = 0
	for i in range(0,30):
		if maxReceived[i] == max(maxReceived):
			maxnum = i
		if maxReceived[i] == min(maxReceived):
			minnum = i
	if cast == 1:
		print("Nomer", x, "e poluchil nai-mnogo(",max(maxReceived),")puti ot nomer", maxnum)
	elif cast == 6:
		print("Nomer", x, "e poluchil nai-malko(",min(maxReceived),")puti ot nomer", minnum)
		
while True:
	os.system('cls')
	val = drawMenu()
	if val == 1:
		mostPopular()
		os.system("PAUSE")
	elif val == 2:
		leastPopular()
		os.system("PAUSE")
	elif val == 3:
		for i in range(1,30):
			mostSend(i, 1)
		os.system("PAUSE")
	elif val == 4:
		for i in range(1,30):
			mostReceived(i, 1)
		os.system("PAUSE")
	elif val == 5:
		for i in range(1,30):
			mostSend(i, 5)
		os.system("PAUSE")
	elif val == 6:
		for i in range(1,30):
			mostReceived(i, 6)
		os.system("PAUSE")
	elif val == 7:
		break
	else:
		continue
	
	
	
	