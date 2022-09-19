import random


def func_first(a: int, b: int):
    sum_a_b = a + b
    if sum_a_b == 7 or sum_a_b == 11:
        return 'you won'
    elif sum_a_b == 2 or sum_a_b == 3 or sum_a_b == 12:
        return "You lost"
    elif sum_a_b == 4 or sum_a_b == 5 or sum_a_b == 6 or sum_a_b == 8 or sum_a_b == 9 or sum_a_b == 10:
        return sum_a_b


def new_game_print():
    print('-----------------------------')
    print('----------NEW GAME ----------')
    print('-----------------------------')

    


def play():
    first_roll = True
    point = 0  # No use
    while True:
        print("Enter 'r' to roll a die OR 'q' to quit OR 'i' for instructions")
        user_choice = input()
        if user_choice == 'r':
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            print(f'[{a},{b}]=>{a + b}')
            if first_roll:
                x = func_first(a, b)
                if type(x) == str:
                    print(x)
                    new_game_print()
                    break
                elif type(x) == int:
                    point = x
            else:
                sum_ = a + b
                if sum_ == 7:
                    print('You lost')
                    new_game_print()
                    break
                elif sum_ == point:
                    print('You won')
                    new_game_print()
                    break
            first_roll = False
        elif user_choice == 'q':
            exit(0)
        elif user_choice == 'i':
            x = """
            You are rolling a dice everytime you enter 'r'.
            The two numbers shown are the upward faces of the dice.
            Also the sum of them will be printed next to the upward faces.
            If the sum is 7 or 11 on the first roll, you win.
            If the sum is 2, 3 or 12 on the first roll, you lose.
            If the sum is 4, 5, 6, 8, 9 or 10 on the first roll, that sum becomes your "point".
            To win, you must continue rolling the dice until you make your point again.
            You lose if u get the sum as 7 before making your point.
            """
            print(x)
            print('-----------------------------')

        else:
            print('Enter a valid input')
            print('-----------------------------')
    play()


play()
