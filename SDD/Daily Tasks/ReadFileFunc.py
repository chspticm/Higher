def readFile(fileName, array):
    txtFile = open(fileName,'r')
    for x in range(len(array)):
        array[x] = txtFile.readline().strip()
    txtFile.close()
    return array

def main():
    name = ['' for x in range(10)]
    name = readFile('names.txt',name)
    print(name)
    
main()