""" A)Naveen is looking for his dream job in the United States, but has some restrictions. He loves New Jersey and
would take a job there if it paid over 40,000 a year. He hates Alabama and demands at least 100,000 to work there.
Any other place he likes to work if paid 60,000 a year, otherwise he is intended to find something better. """
salary = float(input('Enter the amount that Naveen will be paid: '))
if 40000 < salary <= 60000:
	print('Naveen can work in New Jersey')
elif 60000 < salary <= 100000:
	print('Naveen can work anywhere')
elif salary > 100000:
	print('Naveen can work in New Jersey,Alabama or anywhere')
else:
	print('Naveen will find something better')
