# read data from a file

txtFile = open('rolls.txt','r') # opens the file rolls.txt for reading
rolls = [0 for x in range(1000)]

# contents = txtFile.read() # reads the entire contents of the file into the variable contents
for x in range(1000): # loop 1000 times
    rolls[x] = int(txtFile.readline())
    
# print(contents)

txtFile.close()

print(rolls)