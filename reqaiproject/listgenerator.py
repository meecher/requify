import random
import numpy as np
 
draw = random.choices(population=[[0],[1]], weights=[0.5, 0.5], k=80)

#print(draw)

ic0 = 0
ic1 = 0
counter = 0


idlist = np.arange(1, 81, 1)
print(idlist)

rlist0 = [0] * 40
rlist1 = [1] * 40

rlist = rlist0 + rlist1
print(rlist)


for i in rlist1:
    if rlist0[counter] == 0:
        ic0 += 1
    if rlist1[counter] == 1: 
        ic1 += 1
    counter += 1

print("0: " + str(ic0) + "\n 1: " + str(ic1))

counter = 0
randompick = 0
randomid = 0
experimentjoinlist = []
tempjoin = []

for i in idlist:
    randompick = random.randrange(len(rlist))
    randomid = rlist[randompick]
    tempjoin = [idlist[counter]] + [randomid]
    experimentjoinlist.append(tempjoin)
    rlist.pop(randompick)
    counter += 1

print(experimentjoinlist)

for i in experimentjoinlist:
        if i[0] == 1:
            if i[1] == 0:
                print("nai")
            elif i[1] == 1:
                print("ai")

