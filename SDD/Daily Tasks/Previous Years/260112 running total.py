import random
price = [round((random.randint(9,20))/6,2) for x in range(10)]
print(price)

total = 0
for x in range(len(price)):
    total = total + price[x]

print('The total is',round(total,2))