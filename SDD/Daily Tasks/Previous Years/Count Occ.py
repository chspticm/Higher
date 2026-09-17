import random
number = [random.randint(5,19) for x in range(10)]

print(number)

print('What number are you looking for?')
target = int(input('>'))

total = 0
for x in range(10):
    if number[x] == target:
        total = total + 1

print(target,'is in the list',total,'times')