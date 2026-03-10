import random

while True:
    x = input("do you want to roll the dice?(y/n) ").lower()
    print(x)

    if x == "n":
        print("thankyou!!")
        break
    elif x != "y":
        print("invalid choice")
        continue
breakpoint
    y = input("how many dice you want to roll?(1,2) ")
    print(y)

    if y == "2":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')

    elif y == "1":
        die1 = random.randint(1,6)
        print(f'({die1})')

    else:
        print("invalid choice")