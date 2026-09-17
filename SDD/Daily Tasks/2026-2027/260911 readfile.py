# read an array of strings
# Mr Stratton
# 11/09/26

def readFile():
    names = ['' for x in range(15)]
    txtFile = open('rndNames.txt','r')
    for x in range(15):
        names[x] = txtFile.readline().strip()
    
    txtFile.close()
    return names

def readFile2():
    names = ['' for x in range(15)]
    txtFile = open('rndNames.txt','r')
    x=0
    for line in txtFile:    
        names[x] = line.strip()
        x = x +1
    
    txtFile.close()
    return names

def display(names):
    for item in names:
        print(item)

def main():
    names =readFile()
    display(names)
    
main()