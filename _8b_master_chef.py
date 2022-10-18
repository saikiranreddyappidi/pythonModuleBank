try:
	w = int(input("Enter no of weeks: "))
	cost = int(input("Enter cost per week: "))
except:
	print("Enter a valid input")
	exit(1)
print('Total amount to be paid: ', w*cost)
