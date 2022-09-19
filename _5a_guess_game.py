from random import randint


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


def func():
    num = randint(1, 1000)
    score = 100
    print("Find the number from 1 to 1000 which I guessed ")

    i = 10
    while i:
        i -= 1
        print("Enter your guess : ", end="")
        n = int(input())
        if n == num:
            print("Congratulations , You guessed the correct number.")
            print(f"Your score is : {score}")
            print("----------------------------------------------")
            response_func()
        elif n > num:
            print(f"{n} is higher than my guess.")
            score -= 10
        elif n < num:
            print(f"{n} is lower than my guess.")
            score -= 10

        if i == 1:
            print("You failed to guess the number in 10 attempts.")
            print(f"The correct guess is {num}")
            print("You lost the game.")
            print("----------------------------------------------")
            response_func()


func()
