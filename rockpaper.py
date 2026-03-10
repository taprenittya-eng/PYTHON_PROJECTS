import random
computer=random.choice(['s','p','r']).lower()
x=input("what is your choice?(s,p,r)")
print(x)
print("computer chose: ",computer)
if x=='s' and computer=='s':
    print("its a draw")
elif x=='p' and computer=='p':
    print("its a draw")
elif x=='r' and computer=='r':
    print("its a draw")
elif x=='r' and computer=='p':
    print("you lose")
elif x=='r' and computer=='s':
    print("you win")
elif x=='s' and computer=='r':
    print("you lose")
elif x=='s' and computer=='p':
    print("you win")
elif x=='p' and computer=='r':
    print("you win")
elif x=='p' and computer=='s':
    print("you lose")
else:
    print("its invalid choice")