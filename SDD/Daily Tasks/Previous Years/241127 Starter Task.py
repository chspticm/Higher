# What does this program do?
# Describe the purpose of each block of code

import random

roll = [random.randint(1,6) for x in range(1000)]
sides = [0 for x in range(6)]

for side in range(1,7):
    for x in range(1000):
        if roll[x] == side:
            sides[side-1] +=1
            
luckiest = 0
for x in range(0,6):
    print(x+1,'-',sides[x])
    if sides[x] > sides[luckiest]:
        luckiest = x

print('The luckiest dice is',luckiest+1)
   