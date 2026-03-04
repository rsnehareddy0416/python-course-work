'''import csv
with open('sample.csv','a',newline='\n') as file:
    data=csv.writer(file)
    data.writerow(['6',"sneha"])
    data.writerow(['7',"rishika"])'''




'''import csv
with open('products.csv','w',newline='') as file:
    data=csv.writer(file)
    data.writerow(['Product_Ids','Product','Price'])
    data.writerow(['1','laptop','52000'])
    data.writerow(['2','charger','2000'])
    data.writerow(['3','Mouse','500'])
    data.writerow(['4','Tab','32000'])
    print(data)
    '''

import csv
with open('sample.csv','r')as file:
    data=csv.reader(file)
    for row in data:
        print(row[1])