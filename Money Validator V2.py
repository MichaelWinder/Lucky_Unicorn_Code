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
    balance = float(input("How much money do you want to put in?\n(Max is 10, Min is 1): "))
    while balance not in range(1, 11):
        balance = float(input("\nHow much money do you want to put in?\n(Max is 10, Min is 1, Also don't use decimals): "))
    cash_yes_no = yes_no_checker(f"You have chosen to play with ${balance}\nIs that correct?")
    if cash_yes_no == "Yes":
        return balance
    else:
        print()
        balance_set()


balance2 = balance_set()
