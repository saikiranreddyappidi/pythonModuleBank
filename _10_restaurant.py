import random
menu = '''
0.  Enter 0 to exit.
1.	List of students who ordered both biryani and starters.
2.	List of students who order either biryani or starters but not both.
3.	Number of students who order neither biryani nor starters.
4.	Number of students who order biryani and starters but not coke.
5.	Number of students who order only biryani.
6.	Number of students who order both biryani, starters and coke.
7.	Number of students who order only coke.
8.	Number of students who order only starters.
9.  Discard an element.
10. Remove an element.
'''

biryani = set()
starters = set()
coke = set()
total = set()
for i in range(50):
	total.add(i)
for i in range(10):
	biryani.add(random.randint(1, 50))
	starters.add(random.randint(1, 50))
	coke.add(random.randint(1, 50))
print("This values are computer generated")
print("Total: ", total)
print("Biryani: ", biryani)
print("Starters: ", starters)
print("Coke: ", coke)
while True:
	print(menu)
	choice = int(input('Enter your choice: '))
	if choice == 0:
		exit(5)
	elif choice == 1:
		print(biryani.intersection(starters))
	elif choice == 2:
		print(biryani.union(starters) - biryani.intersection(starters))
	elif choice == 3:
		print(total - biryani - starters, "\tNo of students: ", len(total - biryani - starters))
	elif choice == 4:
		print(biryani.union(starters) - coke, "\tNo of students: ", len(biryani.union(starters) - coke))
	elif choice == 5:
		print(biryani - starters.union(coke), "\tNo of students: ", len(biryani - starters.union(coke)))
	elif choice == 6:
		print(biryani.union(starters, coke), "\tNo of students: ", len(biryani.union(starters, coke)))
	elif choice == 7:
		print(coke - biryani.union(starters), "\tNo of students: ", len(coke - biryani.union(starters)))
	elif choice == 8:
		print(starters - biryani.union(coke), "\tNo of students: ", len(starters - biryani.union(coke)))
	elif choice == 9:
		value = int(input('Enter an element to be discarded: '))
		total.discard(value)
		print("Total: ", total)
	elif choice == 10:
		value = int(input('Enter an element to be removed: '))
		try:
			total.remove(value)
		except:
			print(f"An error occurred while removing {value} from total set")
		print("Total: ", total)
	else:
		print("Enter a valid choice.")
