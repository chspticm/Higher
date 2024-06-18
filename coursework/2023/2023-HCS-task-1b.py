# 2023 Higher Computing Coursework

def readfile(attraction, category,visitors,daysOpen, height):
    csvFile = open("attractions.csv","r")
    for x in range(26):
        a,b,c,d,e = csvFile.readline().strip().split(",")
        attraction[x] = a
        category[x] = b
        visitors[x] = int(c)
        daysOpen[x] = int(d)
        height[x] =  e
        
    csvFile.close()
    return attraction, category,visitors,daysOpen, height

def display(attraction, visitors):
    leastPos=0
    mostPos=0
    for x in range(1,26):
        if visitors[x]>visitors[mostPos]:
            mostPos = x
        if visitors[x]<visitors[leastPos]:
            leastPos= x
    
    for x in range(26):
        if visitors[x]==visitors[mostPos]:
            print(attraction[x], "has the most visitors")
        elif visitors[x]==visitors[leastPos]:
            print(attraction[x], "has the least visitors")
            
def writeFile(attraction, category, daysOpen):
    csvFile = open("service.csv","w")
    for x in range(26):
        if category[x] == "Roller Coaster":
            days = daysOpen[x]%90
            if (90 - days) <= 7:
                csvFile.write(attraction[x] + "\n")
                
    csvFile.close()
    
def countOcc(height):
    total = 0
    for x in height:
        if x[0]=="1":
            total=total+1
    print("The number of attractions with a height restriction of 1m and above is",total)

def main():
    #parkSize=26
    attraction = ["" for x in range(26)] # attraction name
    category = ["" for x in range(26)] # category of attraction
    visitors = [0 for x in range(26)] # total number of visitors
    daysOpen = [0 for x in range(26)] # number of days open
    height = ["" for x in range(26)] # height restriction

    # read data from the file into parallel arrays
    attraction, category,visitors,daysOpen, height = readfile(attraction, category,visitors,daysOpen, height)
    
    #Find and display the names of the least visited and most visited attractions
    display(attraction, visitors)
    
    #Write to file the names of roller coasters that need a service within 7 days
    writeFile(attraction, category, daysOpen)
    
    # Task 1d The theme park’s manager wants an update on attractions with a height restriction of 1.0m and above. Height restrictions range from 0.9m to 1.4m
    countOcc(height)
    
main()