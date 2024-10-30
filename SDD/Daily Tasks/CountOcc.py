import random
number = [random.randint(1,100) for x in range(10000)]
print(number)

total = 0
for x in range(len(number)):
    if number[x] >= 50:
        total = total + 1

print('There are',total,'numbers greater than or equal to 50')

total = 0
for n in number:
    if n >= 50:
        total += 1

print('There are',total,'numbers greater than or equal to 50')