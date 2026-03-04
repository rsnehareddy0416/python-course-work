import random
def dice():
    return random.randint(1,100)
user=input("Enter user name:").title()
cur_dice=dice()
print(f'Dice:{cur_dice}')
for i in range(1,8):
    n=int(input())
    if n>cur_dice:
        print("Higher")
    elif n<cur_dice:
        print("Lower")
    else:
        print("You won the game")
        break
else:
    print("you have only 7 attempts")
    