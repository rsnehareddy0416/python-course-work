with open('sample.txt','w') as file:
    file.write('Override')


with open('sample.txt','a') as file:
    file.write('Override')


with open('sample.txt','r') as file:
    file.write('Override')
    print(content)
