def readCSV(array1, array2):
    csvFile = open('names.csv','r')
    for x in range(10):
        a, b = csvFile.readline().strip().split(',')
        
        array1[x] = a
        array2[x] = b
      
    csvFile.close()
    
    return array1, array2

def displayTab(forename, surname):
    print('Forename'.ljust(15) + 'Surname')
    for x in range(10):
        print(forename[x].ljust(15) + surname[x])
        
def main():
    # 0 Set up Varaibles
    forename = ['' for x in range(10)]
    surname = ['' for x in range(10)]
    
    # 1 Read CSV File (out: forename(), surname() )
    forename,surname = readCSV(forename,surname)
    # 2 Display Names (in: forename(), surname() )
    displayTab(forename, surname)

main()