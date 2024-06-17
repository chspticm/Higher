# How to use the debugging tools

import random

total = 0 
count = 0

while True:
    total = total + random.randint(1,100)
    count = count + 1
    if total > 2000:
        print(count)
        break