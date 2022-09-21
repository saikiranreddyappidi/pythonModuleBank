"""Raju is maintaining a medical store, by using python help him to manage the store"""
menu = '''
0. Enter 0 to exit
1. Update the medicines based on availability
2. Display the count of tablet available
3. Display the names of syrups available
4. Display the medicine that is available in both tablet and syrup form
5. Display no of retailers available
6. Display all the medicines available in store
7. Display the amount of all medicines in the store
'''
update_menu = '''
a. To add medicine in tablets
b. To reduce medicine in tablets
c. To add medicine in syrups
d. To reduce medicine in syrups
'''
medicine0 = {'id': 0, 'name': 'erythromycin', 'availability': {'tablet': 100, 'syrups': 0}, 'retailers': 5}
medicine1 = {'id': 1, 'name': 'amoxicillin', 'availability': {'tablet': 200, 'syrups': 400}, 'retailers': 3}
medicine2 = {'id': 2, 'name': 'doxycycline', 'availability': {'tablet': 300, 'syrups': 300}, 'retailers': 8}
medicine3 = {'id': 3, 'name': ' cephalic', 'availability': {'tablet': 400, 'syrups': 200}, 'retailers': 2}
medicine4 = {'id': 4, 'name': 'clindamycin', 'availability': {'tablet': 500, 'syrups': 100}, 'retailers': 10}
details = [medicine0, medicine1, medicine2, medicine3, medicine4]
while True:
	print(menu)
	choice = int(input('Enter your choice: '))
	if choice == 0:
		exit(5)
	elif choice == 1:
		name = int(input('Enter medicine id: '))
		for i in details:
			# try:
			if i['id'] == name:
				print(i)
				print(update_menu)
				reply = input('\t\tEnter your choice: ')
				if reply == 'a':
					amount = int(input('\t\tEnter amount: '))
					i['availability']['tablet'] += amount
				elif reply == 'b':
					amount = int(input('\t\tEnter amount: '))
					i['availability']['tablet'] -= amount
				elif reply == 'c':
					amount = int(input('\t\tEnter amount: '))
					i['availability']['syrups'] += amount
				elif reply == 'd':
					amount = int(input('\t\tEnter amount: '))
					i['availability']['syrups'] -= amount
				else:
					print("Can't do it now")
	# except:
	# 	if i['name'] == name:
	# 		print(i)
	# 		print(update_menu)
	# 		reply = input('\t\tEnter your choice: ')
	# 		if reply == 'a':
	# 			amount = int(input('\t\tEnter amount: '))
	# 			i['availability']['tablet'] += amount
	# 		elif reply == 'b':
	# 			amount = int(input('\t\tEnter amount: '))
	# 			i['availability']['tablet'] -= amount
	# 		elif reply == 'c':
	# 			amount = int(input('\t\tEnter amount: '))
	# 			i['availability']['syrups'] += amount
	# 		elif reply == 'd':
	# 			amount = int(input('\t\tEnter amount: '))
	# 			i['availability']['syrups'] -= amount
	# 		else:
	# 			print("Can't do it now")
	elif choice == 2:
		count = 0
		for i in details:
			print(i['availability']['tablet'])
			count += i['availability']['tablet']
		print('Total no of tablets available: ', count)
	elif choice == 3:
		for i in details:
			if i['availability']['syrups'] > 0:
				print(i['name'])
	elif choice == 4:
		for i in details:
			if i['availability']['tablet'] > 0 and i['availability']['syrups'] > 0:
				print(i['name'])
	elif choice == 5:
		count = 0
		for i in details:
			count += i['retailers']
		print("No of retailers available: ", count)
	elif choice == 6:
		for i in details:
			print(i)
	elif choice == 7:
		total = 0
		for i in details:
			total += (i['availability']['tablet'] + i['availability']['syrups'])
		print('Amount of all medicines available: ', total)
	else:
		print('Enter correct choice')
