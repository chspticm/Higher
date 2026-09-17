def readFile():
    name = []
    online=[]
    peak=[]
    donation=[]
    
    csvFile = open('zoo.csv','r',encoding='utf-8')
    csvFile.readline()
    for line in csvFile:
        a,b,c,d = line.strip().split(',')
        name.append(a)
        online.append(float(b[1:]))
        peak.append(float(c[1:]))
        donation.append(d)
    csvFile.close
    print(name,online,peak,donation)

readFile()