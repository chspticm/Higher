# Reading from text file - Single Value
# Read the contents of file1.txt and display them on screen
# Mr Stratton
# 04/11/24

def readfile():
    txtFile = open('file1.txt','r')
    text = txtFile.read()
    txtFile.close()
    
    return text

def main():
    print(readfile())
    
main()