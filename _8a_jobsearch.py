""" A)Naveen is looking for his dream job in the United States, but has some restrictions. He loves New Jersey and
would take a job there if it paid over 40,000 a year. He hates Alabama and demands at least 100,000 to work there.
Any other place he likes to work if paid 60,000 a year, otherwise he is intended to find something better. """
""" A)Naveen is looking for his dream job in the United States, but has some restrictions. He loves New Jersey and
would take a job there if it paid over 40,000 a year. He hates Alabama and demands at least 100,000 to work there.
Any other place he likes to work if paid 60,000 a year, otherwise he is intended to find something better. """
salary = input('Enter the amount that Naveen will be paid: ')
try:
	salary = float(salary)
	if salary <= 0:
		print("Salary cannot be negative")
		exit(2)
except:
	print("Invalid input.Try giving input like 1234.567")
	exit(3)
if 40000 < salary <= 60000:
	print('Naveen can work in New Jersey')
elif 60000 < salary <= 100000:
	print('Naveen can work anywhere except')
elif salary > 100000:
	print('Naveen can work in New Jersey,Alabama or anywhere')
else:
	print('Naveen will find something better')
