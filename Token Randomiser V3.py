import random
balance = 100


def randomiser(bal):
    if bal == 0:
        print("\nYou do not have enough money left to play\nTherefore you are no use to us\nGet Out!")
        quit()
    elif bal < 1:
        print("\nYou do not have enough money left to play\nLucky for you I will give you 50c change")
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
        print("\nYou Won a Horse\nYuck!")
    else:
        output = 0
        print("\nYou Won a Donkey\nThat sucks")
    bal += output
    print(f"Your profit is ${output:.2f} and your total balance is ${bal:.2f}\n")
    return bal


balance = randomiser(balance)
# Add play again fuction
print(f"\nYour Final Balance is ${balance:.2f}")
