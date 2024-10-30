# Writing to file
# Mr Stratton
# 18/09/24
def findLargest(array):
    maxPos = 0
    for x in range(1,len(array)):
        if array[x] > array[maxPos]:
            maxPos = x
    return maxPos

def writeFile(message):
    txtFile = open('MaxNo.txt','w')
    txtFile.write(message)
    txtFile.close()

def main():
    import random    
    number = [random.randint(1,1000) for x in range(10)]
    position = findLargest(number)
    #print(number)
    message = str(number[position]) + ' at Position ' + str(position)
    writeFile(message)    

main()