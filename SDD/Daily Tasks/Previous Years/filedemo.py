# Reading and Writing to files demo
# Mr Stratton
# 08/09/25

def writeOne():
    # write a single value to a file
    txtFile = open('one.txt','w')
    txtFile.write('Just the one thing')
    txtFile.close()
    
def readOne():
    txtFile = open('one.txt','r')
    line = txtFile.read() # reads all the contents of the file
    txtFile.close()
    print(line)

def writeMany():
    #Write many things to a file all at once
    txtFile = open('many.txt','w')
    txtFile.write('Line one\n') # \n takes a new line
    txtFile.write('Line two\n')
    for x in range(3,10): # Can be used to write the contents of an array
        txtFile.write('Line ' + str(x) +'\n')
        
    txtFile.close()

def readMany():
    #This is the BAD way
    txtFile = open('many.txt','r')
    line = txtFile.read() # reads all the contents of the file
    txtFile.close()
    print(line)
    
    #This is the good way
    txtFile = open('many.txt','r')
    for line in txtFile: # FOR EACH line in the text file
        print(line.strip()) # remove the \n from the end of the line
    txtFile.close()
    
def writeArray():
    import random
    array = [random.randint(1,6) for x in range(20)]
    txtFile = open('numbers.txt','w')
    for x in range(20):
        txtFile.write(str(array[x])+'\n')
    
    txtFile.close()

def readArray():
    array = [0 for x in range(20)]
    txtFile = open('numbers.txt','r')
    for x in range(20):
        array[x] = int(txtFile.readline().strip())
    txtFile.close()
    
    print(array)
    
def main():
    writeOne()
    writeMany()
    writeArray()
    
    readOne()
    readMany()
    readArray()

main()