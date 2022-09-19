import random


def capital():
	c = random.randint(65, 90)
	return chr(c)


def small():
	c = random.randint(97, 122)
	return chr(c)


def symbol():
	num = random.randint(1, 2)
	if num == 1:
		s = random.randint(32, 47)
		return chr(s)
	else:
		s = random.randint(58, 64)
		return chr(s)


def prime():
	arr = [2, 3, 5, 7]
	i = random.randint(0, 3)
	return arr[i]


def composite():
	arr = [4, 6, 8, 9]
	i = random.randint(0, 3)
	return arr[i]


level = int(input("1-low   2-medium    3-high\nEnter your choice: "))
if level == 1:
	t = 8
elif level == 2:
	t = 12
elif level == 3:
	t = 15
else:
	print("Enter a valid choice.")
password = str(capital()) + str(symbol()) + str(prime())
for i in range(1, t - 3):
	password += str(chr(random.randint(32, 126)))

password += str(composite())
print(password, len(password))
