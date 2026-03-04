
print("Winning rules are:\n Rock vs paper-paper wins\n rock vs scissors-Rock wins\n Paper vs Sciessors-scissors wins")
    
while True:
    print("Enter the your choice:1-Rock\n2-Paper\n3-Scissor")
    user1=int(input("Enter user1_choice:"))
    user2=int(input("Enter user2_choice:"))
    if user1==user2:
        print("---It's Tie---")
    elif (user1==1 and user2==3):
        print("---User1 wins---")
    elif (user1==3 and user2==1):
        print("---User2 wins---")
    elif (user1==2 and user2==1):
        print("---User1 wins---")
    elif (user1==1 and user2==2):
        print("---User2 wins---")
    elif (user1==2 and user2==3):
        print("---User2 wins---")
    else:
        print("---User1 wins---")
        