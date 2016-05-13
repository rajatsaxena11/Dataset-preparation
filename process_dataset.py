# creating a new file out of original data set, given desired count of each label

import csv
import random  

a = input('Enter the data column: ')
b = input('Enter the label column: ')
cnt=input('Enter the count of each label you want in your dataset: ')
a=int(a)
b=int(b)
cnt=int(cnt)

f = open('data.csv')
csv_f = csv.reader(f)
next(csv_f, None)

input_list=list()
label_set = set()
for row in csv_f:
    input_list.append((row[a], row[b]))
    label_set.add(row[b])

for g in label_set:
    print (g)
    
aa = random.shuffle(input_list) 
         
lll =[]

for i in label_set:

    count=cnt
    ll=[]

    for row in input_list:

        if (row[b]== i):
            lll.append((row[a], row[b]))
            ll.append((row[a], row[b]))
            count=count-1
                        
        if (count==0):
            break
    
    while(count>0):
        
        bb = random.shuffle(ll)
        
        for pp in ll:
            
            lll.append((pp[a], pp[b]))
            count=count-1
            
            if (count==0):
                break
            
            
cc = random.shuffle(lll)			

with open('newdata.csv', 'wb') as fd:
    fd_write = csv.writer(fd)
    fd_write.writerows(lll)

f.close()
fd.close()

print ('task done ...')


