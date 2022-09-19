from random import randint
lottery_tickets = []

i = 0
while i < 500:
    n = randint(10000, 99999)
    if n not in lottery_tickets:
        lottery_tickets.append(n)
        i += 1

winner1_index = randint(0, 499)
winner2_index = winner1_index
while winner2_index == winner1_index:
    winner2_index = randint(0, 499)

winner1 = lottery_tickets[winner1_index]
winner2 = lottery_tickets[winner2_index]
print(f'The winners are {winner1} and {winner2}')
