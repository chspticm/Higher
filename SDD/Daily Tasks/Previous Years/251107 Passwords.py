# write a program to read in a list of 100 words
# Mr Stratton
# 07/1/25
import random

def readFile():
    words = ['' for x in range(100)]
    txtFile = open('words.txt','r')
    for x in range(100):
        words[x] = txtFile.readline().strip()
    txtFile.close()
    return words

def genPassword(string):
    
    password = string + str(random.randint(0,9)) + str(random.randint(0,9))
    password = password + chr(random.randint(33,47))
    print(password)
    

def main():
    
    words = readFile()
    genPassword(words[random.randint(0,100)])
    print(words[random.randint(0,100)] + ' ' + words[random.randint(0,100)] + ' ' + words[random.randint(0,100)] ) 

main()