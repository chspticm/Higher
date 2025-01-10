# 2023 Specimen Coursework Task
# Jumping Jacks
# 09/01/25

def getData():
    entryID = ['' for x in range(30)]
    location =['' for x in range(30)]
    forename =['' for x in range(30)]
    surname=['' for x in range(30)]
    jumps=[0 for x in range(30)]
    csvFile = open('athletes.csv','r')
    for x in range(30):
        a,b,c,d,e = csvFile.readline().strip().split(',')
        entryID[x] = a
        location[x] = b
        forename[x] = c
        surname[x] = d
        jumps[x] = int(e)
    csvFile.close()
    return entryID, location, forename, surname, jumps 

def genBibs(entryID, location, forename, surname):
    csvFile = open('bibValues.csv','w')
    for x in range(30):
        bibValue = forename[x][0] + surname[x] + str(ord(location[x][0]))
        csvFile.write(entryID[x] + ',' + bibValue + '\n')
    csvFile.close()

def highest(jumps):
    maxJumps = jumps[0]
    for x in range(1,30):
        if jumps[x] > maxJumps:
            maxJumps = jumps[x]
    
    return maxJumps

def display(maxJumps,forename,surname,jumps):
    for x in range(30):
        if jumps[x] == maxJumps:
            print(forename[x],surname[x])
            
        
def finalists(location):
        
    for town in ['Coatbridge','Inverness','Kirkcaldy','Motherwell']:
        total = 0
        for x in range(30):
            if town == location[x]:
                total = total + 1
        print(town,'has', total,'finalists')
    
def main():
    
    #1. Get qualifying athletes’ data
    entryID, location, forename, surname, jumps = getData()
    
    #2. Generate bib values and write to new file with entry IDs
    genBibs(entryID, location, forename, surname)
    
    #3. Find the highest number of jumping jacks completed
    maxJumps = highest(jumps)
    
    #4. Display the full name of the athlete(s) who completed the highest number of jumping jacks
    display(maxJumps,forename,surname,jumps)
    
    # 5. Display Finalists
    finalists(location)
    
main()