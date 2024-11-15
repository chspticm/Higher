# Mr Stratton
# 15/11/24
# 2023 CW Task 1C
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

def findAttactions(attraction,visitors):
    least = visitors[0]
    most = visitors[0]
    for x in range(1,26):
        if visitors[x] > most:
            most = visitors[x]
        if visitors[x] < least:
            least = visitors[x]
            
    for x in range(26):
        if visitors[x] == most:
            print(attraction[x],'Has the most visitors, with',visitors[x],'visiting')
        if visitors[x] == least:
            print(attraction[x],'Has the least visitors, with',visitors[x],'visiting')
        
    

def main():
    attraction = ['' for x in range(26)]
    category = ['' for x in range(26)]
    visitors = [0 for x in range(26)]
    daysOpen = [0 for x in range(26)]
    height = ['' for x in range(26)]
    
    # 1 Read data from file into parallel arrays (OUT attraction(), category(), visitors(), daysOpen(), height() )
    attraction, category, visitors, daysOpen, height = readData(attraction, category, visitors, daysOpen, height)
    # 2 Find and display the names of the least visited and most visited attractions ( IN attraction(), visitors())
    findAttactions(attraction,visitors) 
    # 3 Write to file the names of roller coasters that need a service within 7 days ( IN attraction(), category(), daysOpen())
    pass

main()