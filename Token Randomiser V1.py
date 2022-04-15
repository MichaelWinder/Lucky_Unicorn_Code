import random

balance = 10


def randomiser(bal):
    bal = bal - 1
    token = random.randint(1, 4)
    if token == 4:
        output = 5
    elif token == 3:
        output = 0.5
    elif token == 2:
        output = 0.5
    elif token == 1:
        output = 0
    bal = bal + output
    return bal


print(randomiser(balance))
