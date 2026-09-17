# Write a program that reads in a list of 20 names from a file.
# The names should be split into forename and surname (not allowed to use .split(` `) ).
# The forename and surname should be then written to a CSV file.
# Class Names
# Mr Stratton
# 21/10/24

def getName(name):
    txtFile = open('names.txt','r')
    for x in range(20):
        name[x] = txtFile.readline().strip()
    txtFile.close()
    return name

def search(string, target):
    position = -1
    for x in range(len(string)):
        if string[x] == target:
            position = x
    if position == -1:
        print('Error target not found in string')
    return position  

def splitName(name, forename, surname):
    for x in range(20):
        position = search(name[x],' ')
        forename[x] = name[x][:position]
        surname[x] = name[x][position+1:]  
    
    return forename, surname

def writeCSV(forename, surname):
    csvFile = open('newNames.csv','w')
    for x in range(20):
        line = forename[x] + ',' + surname[x] + '\n'
        csvFile.write(line)
    
    csvFile.close()

def main():
    name = ['' for x in range(20)]
    forename = ['' for x in range(20)]
    surname = ['' for x in range(20)]
    
    name = getName(name)
    forename,surname = splitName(name, forename, surname)
    writeCSV(forename, surname)
    
main()