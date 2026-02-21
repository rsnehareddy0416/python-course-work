play1 = input("Enter the name: ")
play2 = input("Enter the name: ")
n = 5 
play1_count = 0
play2_count = 0
for i in range(5):
    print(f"[r]ock")
    print(f"[p]aper")
    print(f"[s]cissors")
    play1_ch = input("Enter your choice: ")
    play2_ch = input("Enter your choice: ")
    if play1_ch=='r' and play2_ch=='p':
        play2_count = play2_count+1
    elif play1_ch=='r' and play2_ch=='s':
        play2_count = play2_count+1
    elif play1_ch=='p' and play2_ch=='r':
        play1_count = play1_count+1
    elif play1_ch=='p' and play2_ch=='s':
        play2_count = play2_count+1
    elif play1_ch=='s' and play2_ch=='r':
        play2_count = play2_count+1
    elif play1_ch=='s' and play2_ch=='p':
        play1_count = play1_count+1
    elif play1_ch=='r' and play2_ch=='r':
        play1_count = play2_count+1
        play2_count = play2_count+1
    elif play1_ch=='p' and play2_ch=='p':
        play1_count = play2_count+1
        play2_count = play2_count+1
    elif play1_ch=='s' and play2_ch=='s':
        play1_count = play2_count+1
        play2_count = play2_count+1
print(play1_count)
print(play2_count)
if play1_count>play2_count:
    print(f"{play1} won the game!!")
elif play2_count>play1_count:
    print(f"{play2} won the game!!")
else:
    print(f"score is tied {play1},{play2} won the game")
        

       


