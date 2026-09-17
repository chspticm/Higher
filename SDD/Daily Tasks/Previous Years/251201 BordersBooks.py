# Border Books
# 01/12/25
# Mr Stratton
def readCSV():
    title = ['' for x in range(96)]
    author = ['' for x in range(96)]
    price = [0.0 for x in range(96)]
    copies = [0 for x in range(96)]
    lineTotal = [0.0 for x in range(96)]
    
    csvFile = open('borderbooks.csv','r')
    csvFile.readline()
    for x in range(96):
        a,b,c,d = csvFile.readline().strip().split(',')
        title[x] = a
        author[x] = b
        price[x] = float(c)
        copies[x] = int(d)
        lineTotal[x] = round(price[x]*copies[x],2)
        
    csvFile.close()
    return title, author, price, copies, lineTotal

def displayTotal(title,lineTotal):
    total = 0
    for x in range(96):
        print(title[x],lineTotal[x])
        total += lineTotal[x]
    print('The total Revenue was',round(total,2))

def biggestSeller(title,lineTotal):
    # It is assumed that there is only one biggest value
    maxPos = 0
    for x in range(1,len(lineTotal)):
        if lineTotal[x] > lineTotal[maxPos]:
            maxPos = x
    
    print('The biggest earner was',title[maxPos],'with £',lineTotal[maxPos])
    
def biggestSellerV2(title,lineTotal):
    # Is is assumed that two or more books could make the same ammount of money
    maxVal = lineTotal[0]
    for x in range(1,len(lineTotal)):
        if lineTotal[x] > maxVal:
            maxVal = lineTotal[x]
    
    print('These books made £',maxVal)
    for x in range(1,len(lineTotal)):
        if lineTotal[x] == maxVal:
            print(title[x])
    

def main():
    title, author, price, copies, lineTotal = readCSV()
    displayTotal(title,lineTotal)
    biggestSeller(title,lineTotal)
    biggestSellerV2(title,lineTotal)
    

main()