import sys
import random
import os

seat = [[0]*27 for x in range(6)]

def printSeats():
	for r in range(27):
		for c in range(6):
			if seat[c][r] == 0:
				sys.stdout.write("0")
			elif seat[c][r] == 1:
				sys.stdout.write("1")
			elif seat[c][r] == 2:
				sys.stdout.write("2")
			else:
				sys.stdout.write("3")
			if c==2:
				sys.stdout.write("   ")
				
		sys.stdout.write("\n")
	os.system("PAUSE")

def  generatePassengers(): 
	return random.randint(1,3)
	
def	isFull():
	takenSeatsCount = 0
	for c in range(6):
		for r in range(27):
			if seat[c][r] != 0:
				takenSeatsCount += 1
	if takenSeatsCount >= 6*27:
		return True
	else:
		return False
		
def addPassengers(currPassengers):
	totalPassengers = 0
	maxPassengers = 27*6
	isTaken = False
	sys.stdout.write("Current passengers = " + str(currPassengers))
	print("\n")
	for r in range(27):		
		for c in range(6):
			if currPassengers == 1:
				if seat[c][r] == 0:
					seat[c][r] = 1
					isTaken = True

					break
			elif currPassengers == 2:
				if (c!= 2) and (c!= 5) and (seat[c][r] == 0) and (seat[c+1][r] == 0):
					seat[c][r] = 2
					seat[c+1][r] = 2
					isTaken = True
		
					break
			elif currPassengers == 3:
				if (c == 0 or c == 3) and seat[c][r] == 0 and seat[c+1][r] == 0 and seat[c+2][r] == 0:
					seat[c][r] = 3
					seat[c+1][r] = 3
					seat[c+2][r] = 3
					isTaken = True
		
					break
		if isTaken:
			break
	if isTaken:
		totalPassengers += currPassengers
		
#if this was a normal language the main would start from here:
currentPassengers = 0
while not isFull():
	currentPassengers = generatePassengers()
	addPassengers(currentPassengers)
	printSeats()
	
sys.stdout.write("All seats are taken !!!")
os.system("PAUSE")