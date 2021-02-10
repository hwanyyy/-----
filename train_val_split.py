import os

count = 0
length = 10329 #total line

txt = open('list.txt','r')

i = 0

f = open('train.txt','w')
f2 = open('valid.txt','w')

while True :
    if i == 0 :
        line = txt.readline()
        if not line :
            break
        count +=1
        if count < int(length/10)*2 :
            f2.write(line)
        else :
            f.write(line)

txt.close()
f.close()
f2.close()