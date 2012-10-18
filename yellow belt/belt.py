import os
import sys

z = []
for i in range(50):
	z.append(0)
pathToWrite = sys.argv[1]

csv = open("belt1_1.csv", "r")
i = 0
writeTo = open(pathToWrite, "w")
for line in csv:
	arr = line.split(",")
	y = int((int(arr[0])+int(arr[1]))/7)
	writeTo.write(arr[0] +","+ str(int(arr[1]))+"," + str(y) + ",\n")
	i+= 1
