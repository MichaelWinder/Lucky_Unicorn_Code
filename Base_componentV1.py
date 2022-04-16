import random


def deco(text, x):
    sides = "~" * 4
    formatted_text = f"{sides}{text}{sides}"
    if x == 1:
        top_bottom = "*" * len(formatted_text)
    elif x == 2:
        top_bottom = "=" * len(formatted_text)
    elif x == 3:
        top_bottom = "-" * len(formatted_text)
    elif x == 4:
        top_bottom = "#" * len(formatted_text)
    return print(f"{top_bottom}\n{formatted_text}\n{top_bottom}")


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
    if bal == 0:
        print("\nYou do not have enough money left to play\nTherefore you are no use to us\nGet Out!")
        quit()
    elif bal < 1:
        print("\nYou do not have enough money left to play\nLucky for you I will give you 50c change\nGoodbye!")
        quit()
    bal -= 1
    token = random.randint(1, 100)
    if 1 <= token <= 14:
        output = 5
        print("\nYou Won a Unicorn!\nGood Job")
    elif 25 <= token <= 50:
        output = 0.5
        print("\nYou Won a Zebra\nThat's unlucky")
    elif 51 <= token <= 70:
        output = 0.5
        print("\nYou Won a Donkey\nYuck!")
    else:
        output = 0
        print("\nYou Won a Horse\nThat sucks")
    bal += output
    print(f"Your profit is ${output:.2f} and your total balance is ${bal:.2f}\n")
    return bal


def balance_set():
    balance = 99
    while balance not in range(1, 11):
        try:
            balance = float(input("How much money do you want to put in?\n(Max is 10, Min is 1): "))
        except ValueError:
            balance = float(input("How much money do you want to put in?\n(Max is 10, Min is 1): "))
    cash_yes_no = yes_no_checker(f"You have chosen to play with ${balance:.2f}\nIs that correct?")
    if cash_yes_no == "Yes":
        return balance
    else:
        print()
        balance_set()


def instruction():
    return deco("Instructions", 2), print(f"It costs $1 to play a round of Lucky Unicorn"
                                          "\nEach round a token will be generated it will either be a"
                                          "\n-Unicorn $5"
                                          "\n-Zebra   $0.50"
                                          "\n-Donkey  $0.50"
                                          "\n-Horse   $0"
                                          "\nEach of the cash totals equate to how much you receive"
                                          "\nWhen you end the game you will be given your profit\n====================\n")


deco("Welcome to Lucky Unicorn", 1)
play = yes_no_checker("Do you want to play Lucky Unicorn?: ")
if play == "No":
    quit()
instructions = yes_no_checker("\nHave you played Lucky Unicorn Before?: ")
if instructions == "No":
    instruction()
    balance = balance_set()
elif instructions == "Yes":
    balance = balance_set()

highest_number_list = []
highest = None
balance = randomiser(balance)
highest_number_list.append(balance)
while 1 < 10:
    if yes_no_checker(f"Would you like to play another round?: ") == "Yes":
        balance = randomiser(balance)
        highest_number_list.append(balance)
    else:
        for num in highest_number_list:
            if highest is None or num > highest:
                highest = num
        print(f"\nYour Final Balance is ${balance:.2f} and your Highest Balance was ${highest:.2f}")
        quit()
