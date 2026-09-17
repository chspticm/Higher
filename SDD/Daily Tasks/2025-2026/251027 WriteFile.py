# write to a file
# Mr Stratton
# 27/10/2025

def writeFile(forename,surname,age):
    csvFile = open('names.txt','w')
    for x in range(3):
        csvFile.write(forename[x] + ',' + surname[x] + ',' + str(age[x]) + '\n')
    csvFile.close()

def main():
    forename = ['Bob','Sue','John']
    surname = ['Smith','Jones','Adams']
    age = [34,65,32]
    
    writeFile(forename,surname,age)

main()