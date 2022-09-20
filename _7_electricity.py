menu = '''1-Generate a bill    2-Customer having less bill
3-Know about the customer   4-enter 0 to exit\nCost: Rs.10/unit'''
customers = []
print("Customer details(Computer generated): ")
for i in range(10):
	details = {
		'Customerid': i,
		'Customername': str('name') + str(i),
		'units': 10 + i,
		'phno': str(123456789) + str(i),
		'city': str('City') + str(i)
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
session = 0
while True:
	session += 1
	print('--------------------------------------------', f'\n[{session} Session started]')
	print(menu)
	choice = int(input("Enter your choice: "))
	if choice == 1:
		id = int(input('Enter customer id: '))
		for i in customers:
			if i['Customerid'] == id:
				print("Bill amount is: Rs.", i['units'] * 10, '/-')
				break
	elif choice == 2:
		print('Minimum units consumed is ', minimum, ' by ', c_name)
	elif choice == 3:
		parameter = input("Enter customer details[Customer ID/Customer Name]: ")
		for i in customers:
			try:
				if i['Customerid'] == int(parameter):
					print('Customer details based on Customer ID: ')
					required = 'Customer ID: {}   ' \
					           'Customer Name: {}   ' \
					           'Units Consumed: {}  ' \
					           'Phone Number: {}   ' \
					           'city: {}'
					print(required.format(i['Customerid'], i['Customername'], i['units'], i['phno'], i['city']))
					break
			except:
				if i['Customername'] == parameter:
					print('Customer Name: ', i['Customername'])
					print('Customer Ph.no: ', i['phno'])
					break
	elif choice == 0:
		exit(5)
	else:
		print('Enter a valid choice.')
	print(f'[{session} Session ended]', '\n--------------------------------------------')
