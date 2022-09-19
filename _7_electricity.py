menu = '''1-Generate a bill    2-Customer having less bill
3-Know about the customer   4-enter 0 to exit\nCost: Rs.10/unit'''
print(menu)
customers = []
for i in range(10):
	details = {
		'Customerid': i,
		'Customername': str('name') + str(i),
		'units': 10 + i,
		'phno': 100 + i
	}
	customers.append(details)
	print(details)
avg = 0
arr = []
minimum = 10000
for i in customers:
	if minimum > i['units']:
		minimum = i['units']
		c_name = i['Customername']

while True:
	choice = int(input("Enter your choice: "))
	if choice == 1:
		id = int(input('Enter customer id: '))
		for i in customers:
			if i['Customerid'] == id:
				print("Bill amount is: ", i['units'] * 10)
				break
	elif choice == 2:
		print('Minimum units consumed is ', minimum, ' by ', c_name)
	elif choice == 3:
		parameter = input("Enter customer details[Customer ID/Customer Name]: ")
		for i in customers:
			if i['Customerid'] == int(parameter):
				required = 'Customer ID: {}   ' \
				           'Customer Name: {}   ' \
				           'Units Consumed: {}  ' \
				           'Phone Number: {}'
				print(required.format(i['Customerid'], i['Customername'], i['units'], i['phno']))
				break
			elif i['Customername'] == parameter:
				print('Ph.no: ', i['phno'])
				break
	elif choice == 0:
		exit(5)
	else:
		print('Enter a valid choice.')
