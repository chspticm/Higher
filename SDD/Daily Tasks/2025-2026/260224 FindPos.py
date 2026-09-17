import random
array1 = [random.randint(1,1000) for x in range(10)]

print(array1)

def findMaxPos(array):
    maxPos = 0
    for x in range(len(array)):
        if array[x] > array[maxPos]:
            maxPos = x
    
    return maxPos

print('the largest number is', array1[findMaxPos(array1)])
        