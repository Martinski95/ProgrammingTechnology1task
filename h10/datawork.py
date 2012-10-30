import glob
import os
import datetime

homework = [0]*11
homework[0] = 'Предадени входни нива'
homework[1] = 'Направени първоначални хралища с качени задачи'
homework[2] = 'Събиране на числата в шестата колона на csv файл'
homework[3] = 'Събиране на числата в колона в csv файл спрямо числата в друга колона'
homework[4] = 'Добре структуриране хранилище'
homework[5] = 'Въведение в Java. Обработка на аргументи от командния ред'
homework[6]= 'Автоматична подредба на пътници в самолет'
homework[7] = 'Най-популярен ученик в клас'
homework[8] = 'Създаване на съдържание/статия, описващa процеса на commit, pull, push, etc през терминал'
homework[9] = 'Изпит за жълт колан. 18.10.2012. Резултати'

def enterClass():
	bool = True
	while(bool):
		os.system('cls')
		print("Press 1 to select 11 A or 2 to select 11 B, or 3 to print all students in one file.")
		selectedClass = int(input())
		if(selectedClass == 1):
			selectedClass = '11 А'
			bool = False
		elif(selectedClass == 2):
			selectedClass = '11 Б'
			bool = False
		elif(selectedClass == 3):
			selectedClass = 'all'
			bool = False
		else:
			continue
	return selectedClass
	
def enterNumber():
	while(True):
		os.system('cls')
		print("Enter the student number to get his results.")
		number = int(input())
		if(number > 0 and number < 29):
			return number
			break
		else:
			continue

def parseClass(str_class):
	str_class = str_class.strip()
	str_len = len(str_class)
	if(str_len >= 1):
		if((str_class[str_len-1] == 'а' or str_class[str_len-1] =='А' or str_class[str_len-1] =='a' or str_class[str_len-1] =='A')):
			new_str_class = '11 А'#cyrilic
		elif((str_class[str_len-1] =='б' or str_class[str_len-1] =='Б' or str_class[str_len-1] =='B' or str_class[str_len-1] =='b')):
			new_str_class = '11 Б'#cyrilic
		else:
			new_str_class = 'Error with class'
	else:
		new_str_class = 'No class specified'
	return new_str_class
	
def parseEmail(str_email):
	str_email = str_email.strip()
	if(str_email.find('@') != -1):
		return str_email
	else:
		return 'грешен имейл'
		
def parseName(str_name):
	if(len(str_name) < 2):
		str_name = "Не е упоменато име"
		return str_name
	str_name = str_name.strip()
	str_name_new = ''
	asd = 0
	for i in range(len(str_name)):
		if(str_name[i] == 'a'):
			str_name_new += 'а' #cyrilic
		elif(str_name[i] == 'A'):
			str_name_new += 'А' #cyrilic
		elif(str_name[i] == 'b'):
			str_name_new += 'б'
		elif(str_name[i] == 'B'):
			str_name_new += 'Б'
		elif(str_name[i] == 'c'):
			if(str_name[i+1] == 'h'):
				str_name_new += 'ч'
				i+=1
			else:
				str_name_new += 'ц'
		elif(str_name[i] == 'C'):
			if(str_name[i+1] == 'h'):
				str_name_new += 'Ч'
				i+=1
			else:
				str_name_new = str_name_new + 'Ц'
		elif(str_name[i] == 'd'):
			str_name_new += 'д'
		elif(str_name[i] == 'D'):
			str_name_new += 'Д'
		elif(str_name[i] == 'e'):
			str_name_new += 'е'
		elif(str_name[i] == 'E'):
			str_name_new += 'Е'
		elif(str_name[i] == 'f'):
			str_name_new += 'ф'
		elif(str_name[i] == 'F'):
			str_name_new += 'Ф'
		elif(str_name[i] == 'g'):
			str_name_new += 'г' 
		elif(str_name[i] == 'G'):
			str_name_new += 'Г'
		elif(str_name[i] == 'h'):
			if(i > 0):
				if((str_name_new[i-1] == 'ч') or (str_name_new[i-1] == 'ш') or (str_name_new[i-1] == 'Ч') or (str_name_new[i-1] == 'Ш')):
					asd = 0
				else:
					str_name_new += 'х'
		elif(str_name[i] == 'H'):
			str_name_new += 'Х'
		elif(str_name[i] == 'i'):
			if(i>0):
				if(len(str_name) - 1 - i > 0):
					if(str_name[i-1] == 'a'):
						str_name_new += 'й'
						i+=1
					elif(str_name[i+1] == 'u'):
						str_name_new += 'ю'
					else:
						str_name_new += 'и' 
				else:
					str_name_new += 'й'
		elif(str_name[i] == 'I'):
			str_name_new += 'И'
		elif(str_name[i] == 'j'):
			if(str_name[i+1] == 'i'):
				str_name_new += 'ж'
		elif(str_name[i] == 'J'):
			if(str_name[i+1] == 'u'):
				str_name_new += 'Ю'
				i+=1
			else:
				str_name_new += 'Й'
		elif(str_name[i] == 'k'):
			str_name_new += 'к'
		elif(str_name[i] == 'K'):
			str_name_new += 'К'
		elif(str_name[i] == 'l'):
			str_name_new += 'л'
		elif(str_name[i] == 'L'):
			str_name_new += 'Л'
		elif(str_name[i] == 'm'):
			str_name_new += 'м'
		elif(str_name[i] == 'M'):
			str_name_new += 'М'
		elif(str_name[i] == 'n'):
			str_name_new += 'н'
		elif(str_name[i] == 'N'):
			str_name_new += 'Н'
		elif(str_name[i] == 'o'):
			str_name_new += 'о'
		elif(str_name[i] == 'O'):
			str_name_new += 'О'
		elif(str_name[i] == 'p'):
			str_name_new += 'п'
		elif(str_name[i] == 'P'):
			str_name_new += 'П'
		elif(str_name[i] == 'q'):
			str_name_new += 'к'
		elif(str_name[i] == 'Q'):
			str_name_new += 'К'
		elif(str_name[i] == 'r'):
			str_name_new += 'р'
		elif(str_name[i] == 'R'):
			str_name_new += 'Р'
		elif(str_name[i] == 's'):
			if(str_name[i+1] == 'h'):
				str_name_new += 'ш'
				i+=1
			else:
				str_name_new += 'с'
		elif(str_name[i] == 'S'):
			str_name_new += 'С'
		elif(str_name[i] == 't'):
			if(str_name[i+1] == 's'):
				str_name_new += 'ц'
				i+=1
			else:
				str_name_new += 'т'
		elif(str_name[i] == 'T'):
			if(str_name[i+1] == 's'):
				str_name_new += 'Ц'
				i+=1
			else:
				str_name_new += 'Т'
		elif(str_name[i] == 'u'):
			if(str_name_new[i-1] == 'ю'):
				asd = 0
			else:
				str_name_new += 'у'
		elif(str_name[i] == 'U'):
			str_name_new += 'У'
		elif(str_name[i] == 'v'):
			str_name_new += 'в'
		elif(str_name[i] == 'V'):
			str_name_new += 'В'
		elif(str_name[i] == 'w'):
			str_name_new += 'в'
		elif(str_name[i] == 'W'):
			str_name_new += 'В'
		elif(str_name[i] == 'x'):
			str_name_new += 'х'
		elif(str_name[i] == 'X'):
			str_name_new += 'Х'
		elif(str_name[i] == 'y'):
			str_name_new += 'й'
		elif(str_name[i] == 'Y'):
			str_name_new += 'Й'
		elif(str_name[i] == 'z'):
			if(str_name[i+1] == 'h'):
				str_name_new += 'ж'
				i+=1
			else:
				str_name_new += 'з'
		elif(str_name[i] == 'Z'):
			if(str_name[i+1] == 'h'):
				str_name_new += 'Ж'
				i+=1
			else:
				str_name_new += 'З'
		else:
			str_name_new += str_name[i]
	return str_name_new

def parseNumber(str_number):
	str_number = str_number.strip()
	if(str_number.isdigit()):
		return int(str_number)
	else:
		return 0
	

#class to describe each student
class Student:
	classID = 0
	id = 0
	name = ''
	email = ''
	belt = ''
	homework_time_taken = ''
	homework_give_date = ''
	homework_is_given_on_time = False
	homework_link = ''
	homework_solved_tasks = 0
	homwork_max_solved_tasks = 0
	homework_language = ''
	
class Homework:
	ID = 0
	name = ''
	deadline = ''

array = [] #array of students
homeworkarr = [] # array of homeworks

def getBelt(student_class, student_number):
	file = open("10.csv", "r", encoding="utf8")
	lineCount = sum(1 for line in file)
	file.seek(0)
	count = 0
	belt = 'white'
	for line in file:
		val = line.split(",")
		if(parseClass(val[1]) == student_class and parseNumber(val[2]) == student_number ):
			if(student_class[3] == 'А'):
				if(val[9] == "Да"):
					belt = "yellow"
				else:
					belt = "white"
			elif(student_class[3] == 'Б'):
				if(val[9] == "Да"):
					belt = "yellow"
				else:
					belt = "white"
	return belt
	
def getClassNumberNameMail(fileNum):
	file = open(str(fileNum)+".csv", "r", encoding="utf8")
	lineCount = sum(1 for line in file)
	file.seek(0)
	count = 0
	for line in file:
		if(count == 0):
			asd = 0
			count += 1
		else:
			val = line.split(",")
			currClass = parseClass(val[1])
			currNumber = parseNumber(val[2])
			currEmail = parseEmail(val[4])
			currName = parseName(val[3])
			if(currClass[len(currClass)-1] == 'А'):
				array[currNumber].classID = currClass
				array[currNumber].id = currNumber
				array[currNumber].name = currName
				array[currNumber].email = currEmail
				array[currNumber].belt = getBelt(currClass, currNumber)
			elif(currClass[len(currClass)-1] == 'Б'):
				array[currNumber+29].classID = currClass
				array[currNumber+29].id = currNumber
				array[currNumber+29].name = currName
				array[currNumber+29].email = currEmail
				array[currNumber+29].belt = getBelt(currClass, currNumber)
			else:
				array[currNumber].classID = "No imformation"
				array[currNumber].id = "No imformation"
				array[currNumber].name = "No imformation"
				array[currNumber].email = "No imformation"
				array[currNumber].belt = getBelt(currClass, currNumber)
			count += 1
	file.close()
	
	
def compareDates(given_date, deadline_date):
	given_date = given_date.strip()
	deadline_date = deadline_date.strip()
	
	temp1 = given_date.split()
	temp2 = deadline_date.split()
	
	date1 = temp1[0]
	time1 = temp1[1]
	date_deadline = temp2[0]
	time_deadline = temp2[1]
	
	date1arr = date1.split("/")
	time1arr = time1.split(":")
	date2arr = date_deadline.split("/")
	time2arr = time_deadline.split(":")
	
	if(int(date1arr[0]) > int(date2arr[0])): # comparing months
		return False # not given on time
	elif(int(date1arr[0]) < int(date2arr[0])):
		return True # given on time
	elif(int(date1arr[0]) == int(date2arr[0])): 
		if(int(date1arr[1]) > int(date2arr[1])): # comparing dates
			return False
		elif(int(date1arr[1]) < int(date2arr[1])):
			return True
		elif(int(date1arr[1]) == int(date2arr[1])):
			if(int(time1arr[0]) > int(time2arr[0])): #comparing hours
				return False
			elif(int(time1arr[0]) < int(time2arr[0])):
				return True
			elif(int(time1arr[0]) == int(time2arr[0])):
				if(int(time1arr[1]) > int(time2arr[1])): #comparing minutes
					return False
				elif(int(time1arr[1]) < int(time2arr[1])):
					return True
				elif(int(time1arr[1]) == int(time2arr[1])):
					if(int(time1arr[2]) > int(time2arr[2])): #comparing seconds
						return False
					elif(int(time1arr[2]) < int(time2arr[2])):
						return True
					elif(int(time1arr[2]) == int(time2arr[2])):
						return True


for i in range(0,60):
	array.append(Student())
for i in range(0, 11):
	homeworkarr.append(Homework())
for i in range(0, 10):
	homeworkarr[i].ID = i+1
	homeworkarr[i].name = homework[i]

homeworkarr[0].deadline = '9/27/2012 10:50:00'
homeworkarr[1].deadline = '10/2/2012 10:50:00'
homeworkarr[2].deadline = '10/2/2012 10:50:00'
homeworkarr[3].deadline = '10/4/2012 10:50:00'
homeworkarr[4].deadline = '10/9/2012 10:50:00'
homeworkarr[5].deadline = '10/10/2012 20:00:00' # java command line
homeworkarr[6].deadline = '10/15/2012 20:00:00' # podredba na samoleti
homeworkarr[7].deadline = '10/17/2012 20:00:00' # nai popularen 4ovek v klas
homeworkarr[8].deadline = '10/22/2012 20:00:00' # tutorial shit
homeworkarr[9].deadline = 'no deadline'

getClassNumberNameMail(4)
getClassNumberNameMail(5)
getClassNumberNameMail(6)
getClassNumberNameMail(7)
getClassNumberNameMail(8)

def processHomeworks(studentID, studentClass, type, studentFile):
	#if(type == 2):
	#	studentFile = open("Student" + str(studentID) + ", " + studentClass + ".csv", "w")
	if(studentClass[3] == 'Б'):
		studentID += 29
	studentFile.write("Клас, Номер, Име, Поща, Колан\n")
	studentFile.write(str(array[studentID].classID) + "," + str(array[studentID].id) + "," + str(array[studentID].name) + "," + str(array[studentID].email) + "," + str(array[studentID].belt) + "\n")
	studentFile.write("Номер на домашно, Заглавие на домашно, Краен срок, Дата на предаване, Предадено ли е на време, Връзки към решените задачи\n")
	for homeworkID in range(1,10):
		file = open(str(homeworkID) + ".csv", "r", encoding="utf8")
		
		array[studentID].homework_string = homework[homeworkID-1]
		for line in file:
			val = line.split(",")
			
			currClass = parseClass(val[1])
			currNumber = parseNumber(val[2])
			currName = parseName(val[3])
			currEmail = parseEmail(val[4])
						
			if(homeworkID == 1):
				if((array[studentID].classID == currClass and array[studentID].email == currEmail) or (array[studentID].classID == currClass and array[studentID].name == currName)):
					array[studentID].homework_given_date = val[0]
					array[studentID].homework_is_given_on_time = compareDates(array[studentID].homework_given_date, homeworkarr[homeworkID-1].deadline)
					if(array[studentID].homework_is_given_on_time):
						array[studentID].homework_is_given_on_time = "Да"
					else:
						array[studentID].homework_is_given_on_time = "Не"
					array[studentID].homework_link = "No link for this homework"
					studentFile.write(str(homeworkID) + "," + homework[homeworkID-1] + "," + homeworkarr[homeworkID-1].deadline + "," + array[studentID].homework_given_date + "," + array[studentID].homework_is_given_on_time + "," + array[studentID].homework_link + "\n")
					break
				else:
					continue
			elif(homeworkID == 2):
				if((array[studentID].classID == currClass and array[studentID].email == currEmail) or (array[studentID].classID == currClass and array[studentID].name == currName)):
					array[studentID].homework_given_date = val[0]
					array[studentID].homework_is_given_on_time = compareDates(array[studentID].homework_given_date, homeworkarr[homeworkID-1].deadline)
					if(array[studentID].homework_is_given_on_time):
						array[studentID].homework_is_given_on_time = "Да"
					else:
						array[studentID].homework_is_given_on_time = "Не"
					array[studentID].homework_link = val[5]
					studentFile.write(str(homeworkID) + "," + homework[homeworkID-1] + "," + homeworkarr[homeworkID-1].deadline + "," + array[studentID].homework_given_date + "," + array[studentID].homework_is_given_on_time + "," + array[studentID].homework_link)
					break
				else:
					continue
			elif(homeworkID == 3):
				if((array[studentID].classID == currClass and array[studentID].email == currEmail) or (array[studentID].classID == currClass and array[studentID].name == currName)):
					array[studentID].homework_given_date = val[0]
					array[studentID].homework_is_given_on_time = compareDates(array[studentID].homework_given_date, homeworkarr[homeworkID-1].deadline)
					if(array[studentID].homework_is_given_on_time):
						array[studentID].homework_is_given_on_time = "Да"
					else:
						array[studentID].homework_is_given_on_time = "Не"
					array[studentID].homework_link = val[5]
					studentFile.write(str(homeworkID) + "," + homework[homeworkID-1] + "," + homeworkarr[homeworkID-1].deadline + "," + array[studentID].homework_given_date + "," + array[studentID].homework_is_given_on_time + "," + array[studentID].homework_link + "\n")
					break
				else:
					continue
			elif(homeworkID == 4):
				if((array[studentID].classID == currClass and array[studentID].email == currEmail) or (array[studentID].classID == currClass and array[studentID].name == currName)):
					array[studentID].homework_given_date = val[0]
					array[studentID].homework_is_given_on_time = compareDates(array[studentID].homework_given_date, homeworkarr[homeworkID-1].deadline)
					if(array[studentID].homework_is_given_on_time):
						array[studentID].homework_is_given_on_time = "Да"
					else:
						array[studentID].homework_is_given_on_time = "Не"
					array[studentID].homework_link = val[5]
					studentFile.write(str(homeworkID) + "," + homework[homeworkID-1] + "," + homeworkarr[homeworkID-1].deadline + "," + array[studentID].homework_given_date + "," + array[studentID].homework_is_given_on_time + "," + array[studentID].homework_link + "\n")
					break
				else:
					continue
			elif(homeworkID == 5):
				if((array[studentID].classID == currClass and array[studentID].email == currEmail) or (array[studentID].classID == currClass and array[studentID].name == currName)):
					array[studentID].homework_given_date = val[0]
					array[studentID].homework_is_given_on_time = compareDates(array[studentID].homework_given_date, homeworkarr[homeworkID-1].deadline)
					if(array[studentID].homework_is_given_on_time):
						array[studentID].homework_is_given_on_time = "Да"
					else:
						array[studentID].homework_is_given_on_time = "Не"
					array[studentID].homework_link = val[5]
					studentFile.write(str(homeworkID) + "," + homework[homeworkID-1] + "," + homeworkarr[homeworkID-1].deadline + "," + array[studentID].homework_given_date + "," + array[studentID].homework_is_given_on_time + "," + array[studentID].homework_link + "\n")
					break
				else:
					continue
			elif(homeworkID == 6):
				if((array[studentID].classID == currClass and array[studentID].email == currEmail) or (array[studentID].classID == currClass and array[studentID].name == currName)):
					array[studentID].homework_given_date = val[0]
					array[studentID].homework_is_given_on_time = compareDates(array[studentID].homework_given_date, homeworkarr[homeworkID-1].deadline)
					if(array[studentID].homework_is_given_on_time):
						array[studentID].homework_is_given_on_time = "Да"
					else:
						array[studentID].homework_is_given_on_time = "Не"
					array[studentID].homework_link = val[5]
					studentFile.write(str(homeworkID) + "," + homework[homeworkID-1] + "," + homeworkarr[homeworkID-1].deadline + "," + array[studentID].homework_given_date + "," + array[studentID].homework_is_given_on_time + "," + array[studentID].homework_link + "\n")
					break
				else:
					continue
			elif(homeworkID == 7):
				if((array[studentID].classID == currClass and array[studentID].email == currEmail) or (array[studentID].classID == currClass and array[studentID].name == currName)):
					array[studentID].homework_given_date = val[0]
					array[studentID].homework_is_given_on_time = compareDates(array[studentID].homework_given_date, homeworkarr[homeworkID-1].deadline)
					if(array[studentID].homework_is_given_on_time):
						array[studentID].homework_is_given_on_time = "Да"
					else:
						array[studentID].homework_is_given_on_time = "Не"
					array[studentID].homework_link1 = val[5]
					array[studentID].homework_link2 = val[8]
					studentFile.write(str(homeworkID) + "," + homework[homeworkID-1] + "," + homeworkarr[homeworkID-1].deadline + "," + array[studentID].homework_given_date + "," + array[studentID].homework_is_given_on_time + "," + array[studentID].homework_link1 + "," + array[studentID].homework_link2)
					break
				else:
					continue
			elif(homeworkID == 8):
				if((array[studentID].classID == currClass and array[studentID].email == currEmail) or (array[studentID].classID == currClass and array[studentID].name == currName)):
					array[studentID].homework_given_date = val[0]
					array[studentID].homework_is_given_on_time = compareDates(array[studentID].homework_given_date, homeworkarr[homeworkID-1].deadline)
					if(array[studentID].homework_is_given_on_time):
						array[studentID].homework_is_given_on_time = "Да"
					else:
						array[studentID].homework_is_given_on_time = "Не"
					array[studentID].homework_link = val[5]
					studentFile.write(str(homeworkID) + "," + homework[homeworkID-1] + "," + homeworkarr[homeworkID-1].deadline + "," + array[studentID].homework_given_date + "," + array[studentID].homework_is_given_on_time + "," + array[studentID].homework_link + "\n")
					break
				else:
					continue
			elif(homeworkID == 9):
				if((array[studentID].classID == currClass and array[studentID].email == currEmail) or (array[studentID].classID == currClass and array[studentID].name == currName)):
					array[studentID].homework_given_date = val[0]
					array[studentID].homework_is_given_on_time = compareDates(array[studentID].homework_given_date, homeworkarr[homeworkID-1].deadline)
					if(array[studentID].homework_is_given_on_time):
						array[studentID].homework_is_given_on_time = "Да"
					else:
						array[studentID].homework_is_given_on_time = "Не"
					array[studentID].homework_link = val[5]
					studentFile.write(str(homeworkID) + "," + homework[homeworkID-1] + "," + homeworkarr[homeworkID-1].deadline + "," + array[studentID].homework_given_date + "," + array[studentID].homework_is_given_on_time + "," + array[studentID].homework_link + "\n")
					break
				else:
					continue
		

currentClass = enterClass()
if(currentClass == 'all'):
	File = open("All students info.csv", "w")
	for i in range(1, 30):
		processHomeworks(i, '11 А', 1, File)
		File.write("-------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
	for i in range(1, 29):
		processHomeworks(i, '11 Б', 1, File)
		File.write("-------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
else:
	currentNumber = enterNumber()
	File = open("Student" + str(currentNumber) + ", " + currentClass + ".csv", "w")
	processHomeworks(currentNumber, currentClass, 2, File)

os.system("PAUSE")
