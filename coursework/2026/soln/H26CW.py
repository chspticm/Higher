# 2026 Higher Coursework Task
# Mr Stratton
# 15/01/26

def readFile():
    tool = ['' for x in range(120)]
    manufacturer = ['' for x in range(120)]
    dateRented = ['' for x in range(120)]
    returned = ['' for x in range(120)]
    fee = [0 for x in range(120)]
    
    csvFile = open('tools.csv','r')
    for x in range(120):
        line=csvFile.readline().strip()
        a,b,c,d,e =line.split(',')
        tool[x] = a
        manufacturer[x] = b
        dateRented[x] = c
        returned[x] = d
        fee[x] = int(e)
    
    csvFile.close()
    return tool, manufacturer, dateRented, returned, fee

def findTools(tool,manufacturer):
    target = input('Enter a manufacturer: ')
    total = 0
    for x in range(120):
        if manufacturer[x] == target:
            total = total + 1
            print(tool[x])
    print('Total:',total)
    
def calcFees(dateRented,returned,fee):
    for x in range(120):
        if dateRented[x][-4:] == '2025' and returned[x] == 'No':
            if int(dateRented[x][3:5]) >= 1 and int(dateRented[x][3:5]) <= 6:
                fee[x] = 10
            else:
                fee[x] = 5
    return fee

def writeFile(tool,dateRented,fee):
    csvFile = open('lateToosl.csv','w')
    for x in range(120):
        if fee[x] != 0:
            csvFile.write(tool[x]+','+dateRented[x]+','+str(fee[x])+'\n')
    csvFile.close()
    
def main():
    tool, manufacturer, dateRented, returned, fee = readFile()
    findTools(tool,manufacturer)
    fee = calcFees(dateRented,returned,fee)
    writeFile(tool,dateRented,fee)

main()