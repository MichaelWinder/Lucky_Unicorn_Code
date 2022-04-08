yes_no = ""
while yes_no not in ("x", "f"):
    ans = input("Have you played Lucky Unicorn Before?: ").lower()
    while ans not in ("y", "yes", "n", "no"):
        ans = input("Have you played Lucky Unicorn Before?: ")
    else:
        if ans in ("y", "yes"):
            yes_no = "x"
            print("Program continues")
            yes_no = ""
        elif ans in ("n", "no"):
            yes_no = "f"
            print("Program continues")
            yes_no = ""
