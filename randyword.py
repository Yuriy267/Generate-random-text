import random
kolslow =1
colbukv =1
while kolslow < 1000:
    colbutoo = colbukv
    if colbutoo == 1:
        colbukv = int(random.randint(2,7))
    elif colbutoo == 2:
        colbukv = int(random.randint(3, 7))
    else:
        colbukv = int(random.randint(1, 7))

    if colbukv == 2:
        listtwolet = ['an','is','to','on','it','in','if','as','at','of','or','so']
        wordtwolet = random.choice(listtwolet)
        print (wordtwolet, '', end='')
    elif colbukv ==1:
        print ('a','', end='')
    else:
        indexbukva = 0
        slovo = []
        for slogstep in range(colbukv):
            indexbukva += 1
            spisokbukv = ('qwertyuiopasdfghjklzxcvbnm')
            randomfirstbukv = random.choice(spisokbukv)

            if randomfirstbukv in ('eyuioa'):
                randomsecbukv = random.choice('qwrtypsdfghjklzxcvbnm')
            else:


                randomsecbukv = random.choice(spisokbukv)
                randomthrebukv = random.choice ('eyuioa')
                listtrirandbuk = randomfirstbukv + randomsecbukv + randomthrebukv
                slog = (randomfirstbukv, randomsecbukv, randomthrebukv)
            if indexbukva == 1:
                mainbukva = randomfirstbukv
            elif indexbukva == 2:
                mainbukva = randomsecbukv
            elif indexbukva == 3:
                mainbukva = randomthrebukv
            elif indexbukva == 4:
                mainbukva = randomfirstbukv
            elif indexbukva == 5:
                mainbukva = randomsecbukv
            elif indexbukva == 6:
                mainbukva = randomthrebukv
            else:
                mainbukva = randomfirstbukv
            slovo.append(mainbukva)
        #print(slovo)
        for steklovo in range (colbukv):
            print(slovo[steklovo], end='')
        print(' ', end='')



        slogstep += 1





    kolslow +=1
