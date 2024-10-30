# Weather
# Mr Stratton
# 07/10/24

def readData(mon,tue,wed,thur,fri):
    csvFile = open('weather.csv','r')
    for week in range(4):
        a,b,c,d,e = csvFile.readline().strip().split(',')
        mon[week] = int(a)
        tue[week] = int(b)
        wed[week] = int(c)
        thur[week] = int(d)
        fri[week] = int(e)
    csvFile.close()
    return mon,tue,wed,thur,fri

def avgArray(array):
    #print(array)
    total = 0
    for x in range(len(array)):
        total += array[x]
    #print(total)
    return total/len(array)

def display(mon,tue,wed,thur,fri):
    print('Week'.ljust(5),'Mon'.ljust(5),'Tue'.ljust(5),'Wed'.ljust(5),'Thur'.ljust(5),'Fri'.ljust(5),'Avg'.ljust(5))
    for x in range(4):
        week = [mon[x],tue[x],wed[x],thur[x],fri[x]]
        print(str(x+1).ljust(5),str(mon[x]).ljust(5),str(tue[x]).ljust(5),str(wed[x]).ljust(5),str(thur[x]).ljust(5),str(fri[x]).ljust(5), str(avgArray(week)).ljust(5))
    print('Avg'.ljust(5),str(avgArray(mon)).ljust(5),str(avgArray(tue)).ljust(5),str(avgArray(wed)).ljust(5),str(avgArray(thur)).ljust(5),str(avgArray(fri)).ljust(5))

def main():
    # 0 set up arrays and variables
    mon =  [0 for x in range(4)]
    tue =  [0 for x in range(4)]
    wed =  [0 for x in range(4)]
    thur = [0 for x in range(4)]
    fri =  [0 for x in range(4)]
    # 1 read in weather data from file (out: mon,tue,wed,thur,fri)
    mon,tue,wed,thur,fri = readData(mon,tue,wed,thur,fri)
    # 2 display data (in: mon,tue,wed,thur,fri)
    display(mon,tue,wed,thur,fri)

main()