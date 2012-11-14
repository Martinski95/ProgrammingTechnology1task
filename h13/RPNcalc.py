"""
Технологично училище „Електронни системи” http://www.elsys-bg.org/
11 А
17
Мартин Красимиров Кирилов
Да се реализира калкулатор с обратен полски запис.
"""

import os

while(True):
	os.system('cls')
	print("To exit press Enter")
	print("To use the calculator enter your equation and press Enter")
	inputStr = input("Enter your equation in reversed polish notation: ")
	if(inputStr == ""):
		break
	list = inputStr.split()
	stack = []
	listLen = len(list)
	for i in range(0, listLen):
		if(list[i].isdigit()):
			stack.insert(listLen-1, float(list[i]))
		else:
			val1 = float(stack.pop())
			val2 = float(stack.pop())
			if(list[i] == "+"):
				res = val1 + val2
				stack.insert(listLen-1, res)
			elif(list[i] == "-"):
				res = val2 - val1
				stack.insert(listLen-1, res)
			elif(list[i] == "*"):
				res = val1 * val2
				stack.insert(listLen-1, res)
			elif(list[i] == "/"):
				if(val1 == 0.0):
					print("Division by zero!")
					os.system("PAUSe")
					break
				else:
					res = val2 / val1
					stack.insert(listLen-1, res)
			else:
				print("Unknown operator!")
				os.system("PAUSE")
				break
	print("Result: " + str(stack))
	os.system("PAUSE")