a, b, c = map(int, input('Enter the weights of three bags: ').split())
d, e = map(int, input('Enter the airline restricted weights[Checkin weight,Carry weight]: ').split())
if (a + b < d and c < e) or (a + c < d and b < e) or (b + c < d and a < e):
	print('Possible')
else:
	print('Not possible')
