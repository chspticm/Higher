# Find Number in List
# Mr Stratton
# 26/8/24

# 0. set up variables and arrays
from random import *
numbers = [randint(1,100) for x in range(10)]
    
# 1. Get the target for the search
print(numbers)
print('please enter the number to search for')
target = int(input('>'))
# 2. For each item in the list
for x in range(len(numbers)):
# 3. 		if item = target
    if numbers[x] == target:
# 4. 			display number
        print(x)
# 5. 		end if
# 6. next