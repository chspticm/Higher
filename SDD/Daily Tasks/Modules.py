def readFile(array):
    txtFile = open('names.txt','r')
    for x in range(len(array)):
        array[x] = txtFile.readline().strip()
    txtFile.close()
    return array