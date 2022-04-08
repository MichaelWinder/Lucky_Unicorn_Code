def Yes_No_Checker():
    ans = input("Have you played Lucky Unicorn Before?: ").lower()
    print(ans)
    while ans not in ("y", "yes", "n", "no"):
        ans = input("Have you played Lucky Unicorn Before?: ")
    else:
        if ans in ("y", "yes"):
            return "x"
        elif ans in ("n", "no"):
            return "f"


yes_no = (Yes_No_Checker())
if yes_no == "x":
    print("yes")
elif yes_no == "f":
    print("no")
