menu = """a) The average score of class
b) The Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display the no, of students in the specific range
e) Enter e to exit.
"""
print(menu)
marks = []
for i in range(10):
	student = {'Name': str(i), 'Score': 80 + i}
	marks.append(student)
avg = 0
arr = []
absent = 0
for i in marks:
	avg += i['Score']
	arr.append(i['Score'])
	if i['Score'] < 0:
		absent += 1
avg = avg / len(marks)
max_marks = max(arr)
min_marks = min(arr)
while True:
	choice = input("Enter your choice: ").lower()
	if choice == 'a':
		print("Avg of class is ", avg)
	elif choice == 'b':
		print('Max:', max_marks, 'Min:', min_marks)
	elif choice == 'c':
		print('Absent', absent)
	elif choice == 'd':
		x, y = map(int, input('Enter the range: ').split())
		cnt = 0
		for i in marks:
			if x <= i['Score'] < y:
				cnt += 1
		print("No of students in the given range is ", cnt)
	elif choice == 'e':
		exit(1)
	else:
		print('Enter a valid choice.')
