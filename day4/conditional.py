
# elif
amount=int(input("Enter the amount:"))
if amount>50000:
    print(f"Go to Investments")
elif amount>20000:
    print(f"Go for the trip")
elif amount>10000:
    print(f"Go for the clubbings")
elif amount>5000:
    print(f"Go for cafe/res")
elif amount>1000:
    print(f"Go for the shopping")
elif amount>500:
    print(f"Go for the movie")
elif amount>100:
    print(f"Go to hotstar subscription")
elif 20<amount<99:
    print(f"Go to street food")
else:
    print(f"better to sleep")

    # if else
    products=["heels","shirts","handbags","laptop","facewash"]
search=input("Enter the item:")
if search in products:
    print(f"{search} is found!\nGo to shop now!!")
else:
    print(f"{search} is not found!\nLook for other things")

    # if 

    followers=[]
print(f"before followers:{followers}")
status=True
if status:
    followers.append("Ravi")
print(f"After followers:{followers}")

# nestedif

data={'satwik':{'status':True,'python':100,'mysql':99,'softskills':80},
      'dileep':{'status':True,'python':80,'mysql':60,'softskills':75},
      'saketh':{'status':False,'python':'none','mysql':'none','softskills':'none'},
      'praveen':{'status':True,'python':33,'mysql':27,'softskills':60}}
user=input("Enter the student name:")
if user in data:
    if data[user]['status']:
        sum=data[user]['python']+data[user]['mysql']+data[user]['softskills']
        avg=sum/3
        if avg>80:
            print(f"congrats {user}\n you got 'A' grade")
        elif avg>60:
            print(f"Better luck {user} !!\nYou got 'B' grade")
        elif avg>40:
            print(f"Need improvement {user}! \nYou got 'C' grade")
        else:
            print(f"{user},failed in the exam.\nBring your parents")
    else:
        print(f"{user} didn't write any exams")


      