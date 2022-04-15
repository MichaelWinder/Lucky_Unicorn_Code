import random

balance = 10


def yes_no_checker(question_text):
    while True:
        ans = input(question_text).lower()
        while ans not in ("y", "yes", "n", "no"):
            ans = input(question_text).lower()
        else:
            if ans in ("y", "yes"):
                return "Yes"
            elif ans in ("n", "no"):
                return "No"


def randomiser(bal):
    bal = bal - 1
    token = random.randint(1, 100)
    if 1 <= token <= 25:
        output = 5
    elif 26 <= token <= 50:
        output = 0.5
    elif 51 <= token <= 75:
        output = 0.5
    elif 76 <= token <= 100:
        output = 0
    bal = bal + output
    return bal


balance = (randomiser(balance))
print(balance)


def playing(variable):
    play_again = yes_no_checker(f"Would you like to play another round you have ${variable} left: ")
    if play_again == "Yes":
        return randomiser(variable)
    elif play_again == "No":
        print(f"money left is {variable}")
        return "No"


balance = playing(balance)
