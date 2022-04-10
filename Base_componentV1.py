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


def balance_set():
    balance = 99
    while balance not in range(1, 11):
        try:
            balance = float(input("How much money do you want to put in?\n(Max is 10, Min is 1): "))
        except ValueError:
            balance = float(input("How much money do you want to put in?\n(Max is 10, Min is 1): "))
    cash_yes_no = yes_no_checker(f"You have chosen to play with ${balance}\nIs that correct?")
    if cash_yes_no == "Yes":
        return balance
    else:
        print()
        balance_set()


play = yes_no_checker("Do you want to play Lucky Unicorn?: ")
if play == "No":
    quit()


def instruction():
    print("====================\n~~~~INSTRUCTIONS~~~~\n\n(enter instructions here)\n\n====================")


instructions = yes_no_checker("\nHave you played Lucky Unicorn Before?: ")
if instructions == "No":
    instruction()
    balance2 = balance_set()
elif instructions == "Yes":
    balance2 = balance_set()
