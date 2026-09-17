# write Array to file
# Mr Stratton
# 11/09/26

def randomArray():
    import random
    array = [0 for x in range(356)]
    for x in range(len(array)):
        array[x] = random.randint(1,92)
    
    return array

def saveToFile(array):
    txtFile = open('numbersArray.txt','w')
    for x in range(len(array)):
        txtFile.write(str(array[x]) + '\n')
    txtFile.close()

def readFile():
    # Read a multiline file in to an array of integers
    array = [0 for x in range(356)]
    txtFile = open('numbersArray.txt','r')
    for x in range(len(array)):
        array[x] = int(txtFile.readline())
    
    txtFile.close()
    return array
    
def main():
    # array = randomArray()
    
    # saveToFile(array)
    array=readFile()
    print(array)
    print(type(array))
    
main()