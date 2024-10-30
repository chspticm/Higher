# CSV Write
# Mr Stratton
# 22/10/24

def getNames(name):
    txtFile = open('names.txt','r')
    for x in range(20):
        name[x] = txtFile.readline().strip()
    txtFile.close()
    
    return name

def search(string, target): # Formal Parameters
    position = 0 
    for x in range(len(string)):
        if string[x] == target:
            position = x
    return position

def splitName(name,forename,surname):
    for x in range(20):
        position = search(name[x], ' ') # Actual Parameters (Arguments)
        forename[x] = name[x][:position]
        surname[x] = name[x][position+1:] # +1 to remove space
    
    return forename,surname

def writeCSV(forename, surname):
    csvFile = open('names.csv','w')
    for x in range(20):
        line = forename[x] + ',' + surname[x] + '\n'
        csvFile.write(line)
    csvFile.close()
    
def main():
    name = ['' for x in range(20)]
    forename = ['' for x in range(20)]
    surname = ['' for x in range(20)]
    # get names
    name = getNames(name) # Call 
    # split names
    forename,surname = splitName(name,forename,surname) # Call
    # write CSV file
    writeCSV(forename, surname)
    
    

main()