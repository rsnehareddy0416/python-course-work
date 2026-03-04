import random
import sys
player1=input("Enter the player1 name:").title()
player2=input("Enter the player2 name:").title()
player1_score,player2_score=0,0
winning_point=100
snakes={16:8,32:20,43:4,50:27,73:32,87:49,98:6,92:77}
ladders={7:24,14:40,25:89,37:42,57:76,79:83}
def dice():
    return random.randint(1,6)
def player1_turn():
    global player1_score
    player1_status=input(f"{player1},You want to [c]ontinue or [q]uit:").lower()
    if player1_status=='c':
        cur_dice=dice()
        print(f'Dice:{cur_dice}')
        player1_score+=cur_dice

        if player1_score>=winning_point:
            print(f'congrats{player1},You won the game!!!')
            sys.exit()

        if player1_score in snakes:
            player1_score=snakes[player1_score]
            print(f'Board position after snake bit:{player1_score}')
        elif player1_score in ladders:
            player1_score=ladders[player1_score]
            print(f'Board position after ladder:{player1_score}')
        else:
            print(f'Board position:{player1_score}')
    else:
        print(f"Game exited")
        sys.exit()
def player2_turn():
    global player2_score
    player2_status=input(f"{player2},You want to [c]ontinue or [q]uit:").lower()
    if player2_status=='c':
        cur_dice=dice()
        print(f'Dice:{cur_dice}')
        player2_score+=cur_dice

        if player2_score >=winning_point:
            print(f'congrats{player2},You won the game!!!')
            sys.exit()
            
        if player2_score in snakes:
            player2_score=snakes[player2_score]
            print(f'Board position after snake bit:{player2_score}')
        elif player2_score in ladders:
            player2_score=ladders[player2_score]
            print(f'Board position after ladder:{player2_score}')
        else:
            print(f'Board position:{player2_score}')
    else:
        print(f"Congrats {player1},You won the game!!!")
        
    
while player1_score<winning_point and player2_score<winning_point:
    player1_turn()
    player2_turn()
