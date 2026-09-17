# 1. numbers =[23,76,45,98,23,65,37,93,71,37,40,21]
numbers = [23,76,45,98,23,65,37,93,71,37,40,21]
# 2. max = numbers [0]
maxPos = 0
maxNo = numbers[maxPos]
# 3. Loop for length of array
for x in range(1, len(numbers)):
# 4.	If numbers [counter] > max then
    if numbers[x] > maxNo:
# 5.		max = numbers [counter]
        maxNo = numbers[x]
        maxPos = x
# 6. Display max to user
print(maxNo, maxPos)