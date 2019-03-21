import os
import random

for i in range(100000):
    colslog = int(random.randint(1, 6))
    #print (' ', end='')

    last_name = ''
    for t in range(colslog):
        q = random.choice('qwrtpsdfghjklzxcvbnm')
        w = random.choice('eyuioa')
        #print (q, end='')
        #print (w, end='')
        slogg = q+w
        #print (slogg, end= '')

        last_name = str(last_name) + slogg

    print (last_name, '', end='')
    #spisok [i-1] = last_name