from random import randint
import sys


def response_func():
    print("Enter 'y' to play again, Enter 'n' to quit : ", end="")
    response = input()
    if response == 'y':
        func()
    elif response == 'n':
        exit(1)
    else:
        print('Enter a valid key')
        response_func()

# -------------------- Code written by ZAARZET -----------------------

''' Testing 
def read_x():
    valid_question = ('a', 'b', 'c')
    print("Enter your guess : ", end=" ")
    arr = input().split()
    try:
        int(arr[0])
        str(arr[1])
    except IndexError:
        print('Invalid input')
        read_x()
    except ValueError:
        print('Invalid input')
        read_x()
    print(arr)
    question = arr[1]
    if question not in valid_question:
        print('Invalid input')
        read_x()
    else:
        return arr
'''


def func():
    u = randint(0, 50)
    attempts = 0
    print("Find the number which I guessed ")
    while True:
        attempts += 1
        # arr = read_x()
        print("Enter your guess : ", end=" ")
        arr = input().split()
        x = int(arr[0])
        question = arr[1]
        print("max : "+str(sys.maxsize))
        print("u : " + str(u))
        if question == 'a':
            print(x > u)
        elif question == 'b':
            print(x < u)
        elif question == 'c':
            print(x == u)
            print(f"Congratulations! You won the game in {attempts} attempts")
            print("----------------------------------------------")
            response_func()
       


func()
