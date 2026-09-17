# 1. numbers = [23, 76, 45, 71, 98, 23, 65, 37, 93, 71, 37, 21] 
# 2. searchValue = 71 
# 3. found = False 
# 4. Loop for length of array  
# 5. If numbers[counter] = searchValue 
# 6.
# 7.   
# Display "Found at position", counter 
# found = True 
# 8. If found equals False then 
# 9.  
# Display "No matches found"

numbers = [23, 76, 45, 71, 98, 23, 65, 37, 93, 71, 37, 21]
found = False
target = 71

for x in range(len(numbers)):
    if target == numbers[x]:
        found = True
        print('found at position',x)

if not found:
    print(target,'is not in the list')

print('============= Efficient Version ==============')
numbers = [23, 76, 45, 71, 98, 23, 65, 37, 93, 71, 37, 21]
found = False
target = 21
index = 0
while not found and index < len(numbers):
    if numbers[index] == target:
        found=True
        print(target,'is in the list')
    else:
        index = index + 1

if not found:
    print(target,'is not in the list')