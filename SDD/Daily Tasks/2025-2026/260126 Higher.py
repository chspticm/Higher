# Higher Spec CW
# 26/01/26

def getData():
    #1. Get qualifying athletes’ data OUT: entryID(), location(), forename(), surname(), jumps()
    #Set up arrays
    entryID = ['' for x in range(30)]
    location = ['' for x in range(30)]
    forename = ['' for x in range(30)]
    surname = ['' for x in range(30)]
    jumps = [0 for x in range(30)]
    
    csvFile = open('athletes.csv','r') # open file for reading
    for x in range(30):
        a,b,c,d,e = csvFile.readline().strip().split(',') # read values
        entryID[x] = a
        location[x] = b
        forename[x] = c
        surname[x] = d
        jumps[x] = int(e)
    
    csvFile.close()
    return entryID, location, forename, surname, jumps

def generate(entryID, location, forename, surname):
    #2. Generate bib values and write to new file with entry IDs IN: entryID(), location(), forename(), surname() 
    csvFile = open('bibValues.csv','w') # open file to write
    for x in range(30):
        bibValue = forename[x][0] + surname[x] + str(ord(location[x][0]))
        csvFile.write(entryID[x] + ',' + bibValue + '\n')
    csvFile.close()

def findHighest(jumps):
    #3. Find the highest number of jumping jacks completed IN: jumps(), OUT:maxJumps
    maxJumps = jumps[0]
    for x in range(1,len(jumps)):# find max
        if jumps[x] > maxJumps:
            maxJumps = jumps[x]
    
    return maxJumps

def display(maxJumps,forename,surname,jumps):
    #4. Display the full name of the athlete(s) who completed the highest number of jumping jacks
    for x in range(30):
        if jumps[x] == maxJumps: # display only athlets with highest jump
            print(forename[x],surname[x])

def findLocation(location):
    for town in ['Coatbridge','Inverness','Kirkcaldy','Motherwell']:
        total = 0
        for x in range(len(location)):
            if location[x] == town:
                total = total + 1
        print(town,'has',total,'finalists')
    
def main():
    entryID, location, forename, surname, jumps = getData()
    generate(entryID, location, forename, surname)
    maxJumps = findHighest(jumps)
    display(maxJumps,forename,surname,jumps)
    findLocation(location)

main()