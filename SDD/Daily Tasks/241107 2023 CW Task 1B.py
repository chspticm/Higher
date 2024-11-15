# 2023 CW task 1B - 5A
# Mr Stratton
# 07/11/24

def readData(attraction, category, visitors, daysOpen, height):
    csvFile = open('attractions.csv','r')
    for x in range(26):
        line = csvFile.readline().strip()
        a,b,c,d,e = line.split(',')
        attraction[x] = a
        category[x] = b
        visitors[x] = int(c)
        daysOpen[x] = int(d)
        height[x] = e
    csvFile.close()
    return attraction, category, visitors, daysOpen, height
 
def findDisplay(attraction, visitors):
    minVal = visitors[0]
    maxVal = visitors[0]
    for x in range(1,26):
        if visitors[x] < minVal:
            minVal = visitors[x]
        if visitors[x] > maxVal:
            maxVal = visitors[x]
    
    for x in range(26):
        if visitors[x] == minVal:
            print(attraction[x],'is the least visited with',visitors[x],'visitors')
        if visitors[x] == maxVal:
            print(attraction[x],'is the Most visited with',visitors[x],'visitors')
            
def writeFile(attraction, category, daysOpen):
    csvFile = open('service.csv','w')
    for x in range(26):
        if category[x] == 'Roller Coaster':
            days = daysOpen[x]%90
            if 90-days <= 7:
                csvFile.write(attraction[x]+'\n')
    
    csvFile.close()
    
def main():
    attraction = ['' for x in range(26)]
    category  = ['' for x in range(26)]
    visitors = [0 for x in range(26)]
    daysOpen = [0 for x in range(26)]
    height = ['' for x in range(26)]
# 1 Read data from file into parallel arrays OUT attraction(), category(), visitors(), daysOpen(), height()
    attraction, category, visitors, daysOpen, height = readData(attraction, category, visitors, daysOpen, height)    
    #print(attraction, category, visitors, daysOpen, height)
# 2 Find and display the names of the least visited and most visited attractions IN attraction(), visitors()
    findDisplay(attraction, visitors)
# 3 Write to file the names of roller coasters that need a service within 7 days IN attraction(), category(), daysOpen()
    writeFile(attraction, category, daysOpen)
    
main()