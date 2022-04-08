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
    balance = input("\nHow much money do you want to put in?\n(Max is 10, Min is 1): ")
    while balance not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
        balance = input("\nHow much money do you want to put in?\n(Max is 10, Min is 1, Also don't use decimals): ")
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

converted_bal = float(balance2)
print(converted_bal)
