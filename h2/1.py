"""
ТУЕС
11 А
17
Мартин Красимиров Кирилов
Да се обработи дадения csv документ, като се сумират стойностите в една колона.
"""

sum = 0;

file = open("zadachi.csv");
for line in file:
	num = line.split(",")[4];
	if num.isnumeric():
		sum += int(num);
 
print("Sum = " + str(sum));
input("Press Enter to exit...");