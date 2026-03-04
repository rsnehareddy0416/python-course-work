import json


'''with open('demo.json','w') as file:
    data=[
        {'id':1,'name':'komali'},
        {'id':2,'name':'sneha'},
        {'id':3,'name':'rishika'}
        ]
    json.dump(data,file,indent=4)
    print("Data saved successfully!")'''

'''with open('demo.json','r') as file:
    data=json.load(file)
    for i in data:
        print(i)
'''

with open('demo.json','r') as file:
    data=json.load(file)
data.append({'id':4,'name':'varsha'})
with open('demo.json','w') as file:
    json.dump(data,file,indent=4)