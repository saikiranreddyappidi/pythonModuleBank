x, y = map(int, input("Enter the price of double and triple rooms: ").split())
print("Minimum amount: ", min(3 * x, 2 * y))
if 3 * x > 2 * y:
	print("Better to get 2 triple rooms")
elif 3 * x < 2 * y:
	print("Better to get 3 double rooms")
else:
	print("Either is good")
