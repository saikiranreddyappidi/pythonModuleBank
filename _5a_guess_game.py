from random import randint


def ahead(c_guess: int, player_guess: int):
    diff = player_guess-c_guess
    if diff >= 500:
        print(f"{player_guess} is too much higher than my guess.")
    elif diff >= 250:
        print(f"{player_guess} is too higher than my guess.")
    else:
        print(f"{player_guess} is higher than my guess.")


def behind(c_guess: int, player_guess: int):
    diff = c_guess - player_guess
    if diff >= 500:
        print(f"{player_guess} is too much lower than my guess.")
    elif diff >= 250:
        print(f"{player_guess} is too lower than my guess.")
    else:
        print(f"{player_guess} is lower than my guess.")


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
            # print(f"{n} is higher than my guess.")
            ahead(num, n)
            score -= 10
        elif n < num:
            # print(f"{n} is lower than my guess.")
            behind(num, n)
            score -= 10

        if i == 1:
            print("You failed to guess the number in 10 attempts.")
            print(f"The correct guess is {num}")
            print("You lost the game.")
            print("----------------------------------------------")
            response_func()
        print(f"{i} chances left.")


func()
