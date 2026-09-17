# 2023 Higher CS coursework task
# 23/02/26
# Mr Stratton

def readData():
    # 1 Read data from file into parallel arrays
    # OUT attraction(), category(), visitors(), daysOpen(), height()
    attraction = ['' for x in range(26)]
    category = ['' for x in range(26)]
    visitors = [0 for x in range(26)]
    daysOpen = [0 for x in range(26)]
    height = ['' for x in range(26)]
    
    csvFile = open('attractions.csv','r')
    for x in range(26):
        a,b,c,d,e = csvFile.readline().strip().split(',')
        attraction[x] = a
        category[x] = b
        visitors[x] = int(c)
        daysOpen[x] = int(d)
        height[x] = e
    
    csvFile.close()
    
    return attraction, category, visitors, daysOpen, height

def findAtt(attraction,visitors):
    
    minAtt = visitors[0]
    maxAtt = visitors[0]
    for x in range(1,len(visitors)):
        if visitors[x] > maxAtt:
            maxAtt = visitors[x]
        if visitors[x] < minAtt:
            minAtt = visitors[x]
    
    for x in range(len(visitors)):
        if visitors[x] == maxAtt:
            print('Max vistied attaction -',attraction[x])
        if visitors[x] == minAtt:
            print('Least vistied attaction -',attraction[x])
    
def createCSV(attraction, category,daysOpen):
    # 3.1 Create ‘service.csv’ file
    csvFile = open('service.csv','w')
    # 3.2 Loop for each attraction
    for x in range(26):
        # 3.3 If current category is ‘Roller Coaster’ then
        if category[x] == 'Roller Coaster':
            # 3.4 Set days to current daysOpen modulus 90
            days = daysOpen[x] % 90
            # 3.5 If (90 – days) is less than or equal to 7 then
            if (90-days) <= 7:
                # 3.6 Write current attraction to file
                csvFile.write(attraction[x]+'\n')
            # 3.7 End if
        # 3.8 End if
    # 3.9 End loop
    # 3.10 Close ‘service.csv’ file
    csvFile.close()

def count(array,target):
    total = 0
    for item in array:
        if item[0] == target:
            total+=1
    print('The total is',total)
    
def main():category, visitors, daysOpen, height = readData()
    findAtt(attraction,visitors)
    createCSV(attraction, category,daysOpen)
    count(height,'1')

main()