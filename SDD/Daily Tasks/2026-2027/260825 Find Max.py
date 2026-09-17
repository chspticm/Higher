# Find Maximum
# Mr Stratton
# 25/08/26

numbers = [223, 76, 45, 98, 23, 65, 37, 93, 171, 37, 40, 21, 1000] # Store a list of numbers

maxNo = numbers[0] # 

for x in range(1,len(numbers)):
    if numbers[x] > maxNo:
        maxNo = numbers[x]

print('The largest number is',maxNo)
    
