import random
number = [random.randint(1,10) for x in range(10)]
print(number)

print('What number are you looking for?')
target = int(input('>'))

found = False
pos = 0 
while not found and pos < len(number):
    if target == number[pos]:
        found = True
    else:
        pos = pos + 1

if found:
    print(target,'found at position',pos)
else:
    print(target, "not found in array")