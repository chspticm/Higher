# Write a program to read in the file rolls.txt
# display how many times a 1 was rolled
# your program should be modular
'''
1. Read in file to array
2. count the number of 1s rolled
3. display the number of 1s rolled
'''

def readFile():
    # read data from a file

    txtFile = open('rolls.txt','r') # opens the file rolls.txt for reading
    rolls = [0 for x in range(1000)]
    
    for x in range(1000): # loop 1000 times
        rolls[x] = int(txtFile.readline())
    
    txtFile.close()
    
    return rolls

def countOcc(array,target):
    count = 0
    for x in range(len(array)):
        if array[x] == target:
            count += 1
    return count

def main():
    rolls = readFile()
    count = countOcc(rolls,1)
    print('The number of 1s is',count)
    
main()