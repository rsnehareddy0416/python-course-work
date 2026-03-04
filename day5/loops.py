#for loop
'''for var in seq:
    stmts:
seq:list,tuple,set,dict,str,range'''

#List
'''products=list(input("Enter the products:").split())
for product in products:
    print(f'{product}-Add to fav | Buy Now | Add to cart')'''

#Tuple
'''sizes=('xs','s','m','l','xl','xxl')
for s in sizes:
    print(f'...|{s}|...')'''

#Set
'''followers={'sakeeth','satwik','dileep','ravi'}
for i in followers:
    print(f'{i}-|follow back|remove|message|')'''

#Dict
'''data={"varsha":["c","python","ml"],"meghana":["python","java","linux"]}
for i in data:
    print(f"{i}:{data[i]}")'''

#str
'''s="python programming"
for i in s:
    print(i,end='')'''


#range(start,stop+1,step)=range(0,n,1)
'''for i in range(0,100,1):
    print(i,end=',')'''

#even numbers from 2 to 100
'''for i in range(2,101,2):
    print(i,end=',')'''

#tables
'''n=int(input("Enter the number:"))
print(f"{n}-Table")
for i in range(1,11):
    print(f'{n}*{i}={n*i}')'''

#break
'''for i in range(1,10):
    if i==7:
        break
    print(i)'''

#continue
'''for i in range(1,10):
    if i==1:
        continue
    print(i)'''

#while loop
'''i=1
while i<=10:
    print(i)
    i=i+1'''

'''moves=15
winning_point=int(input("Tell me how many moves you require:"))
while moves>1:
    if 15 - winning_point==moves:
        print("You won the game")
        break
    print(f"{moves} are left")
    moves-=1
else:
    print("game is over")'''

bullets=10
while bullets>0:
    print(f"You have {bullets} bullets,shoot them!")
    bullets-=1
else:
    print("game is over")



    