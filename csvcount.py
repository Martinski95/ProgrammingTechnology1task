sum = 0;

file = open("zadachi.csv");
for line in file:
	num = line.split(",")[1];
	if num.isnumeric():
		sum += int(num);
 
print("Sum = " + str(sum));
input("Press Enter to exit...");