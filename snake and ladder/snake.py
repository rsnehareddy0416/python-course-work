import random
def dice():
    return random.randint(1,6)

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}


snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}
play1 = input("Enter the name: ")
play2 = input("Enter the name: ")
score_play1 = 0
score_play2 = 0
win_point = 100
while score_play1<100 and score_play2<100:
    ch = input(f"{play1} want to [c]ontinue or [q]uit: ").lower()
    if ch=="c":
        print("continue the game")
    else:
        print(f"{play2} has won the game")
        break
    cur_dice = dice()
    print(f"{play1} rolled the dice and dice given value {cur_dice}")
    score_play1 = score_play1+cur_dice
    if score_play1 in ladders:
        score_play1 = ladders[score_play1]
    if score_play1 in snakes:
        score_play1 = snakes[score_play1]
    if score_play1>100:
        score_play1 = score_play1-cur_dice
    print(f"Now the present score of {play1} ={score_play1}")
    if score_play1==win_point:
        print(f"{play1} won the game")
        break
    ch = input(f"{play2} want to [c]ontinue or [q]uit: ").lower()
    if ch=="c":
        print("continue the game")
    else:
        print(f"{play1} has won the game")
        break
    cur_dice = dice()
    print(f"{play2} rolled the dice and dice given value {cur_dice}")
    score_play2 = score_play2+cur_dice
    if score_play2 in ladders:
        score_play2 = ladders[score_play2]
    if score_play2 in snakes:
        score_play2 = snakes[score_play2]
    if score_play2>100:
        score_play2 = score_play2-cur_dice
    print(f"Now the present score of {play2} ={score_play2}")
    if score_play2==win_point:
        print(f"{play2} won the game")
        break

    

