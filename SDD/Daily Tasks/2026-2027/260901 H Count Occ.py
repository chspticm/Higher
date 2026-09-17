# 1. numbers = (23, 76, 45, 71, 98, 23, 65, 37, 93, 71, 37, 40, 21) 
# 2. above50 = 0 
# 3. Loop for length of array  
# 4.    If numbers[counter] > 50 then 
# 5.        Add 1 to above50 
# 6. Display "The array has ", above50, numbers above 50."

numbers = [23, 76, 45, 71, 98, 23, 65, 37, 93, 71, 37, 40, 21, 50]
above50 = 0

for x in range(len(numbers)):
    if numbers[x] == 50:
        above50 = above50 + 1

print('The array has',above50,'numbers 50.')