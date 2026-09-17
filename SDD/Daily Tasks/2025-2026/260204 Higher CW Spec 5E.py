# Mr Stratton
# 04/02/26
# Specimen CW Task 1 part B


# 2. Generate bib values and write to new file with entry IDs
# 3. Find the highest number of jumping jacks completed
# 4. Display the full name of the athlete(s) who completed the highest number of jumping jacks

def getData():
    # 1. Get qualifying athletes' data
    # set up arrays
    entryID = ['' for x in range(30)]
    location = ['' for x in range(30)]
    forename = ['' for x in range(30)]
    surname = ['' for x in range(30)]
    jumps = [0 for x in range(30)]
    
    csvFile = open('athletes.csv','r') # open file to read from
    for x in range(30):
        line = csvFile.readline().strip()
        a,b,c,d,e = line.split(',') # seperate items
        entryID[x] = a
        location[x] = b
        forename[x] = c
        surname[x] = d
        jumps[x] = int(e)
    
    return entryID, location, forename, surname, jumps

def bibGen(entryID,location,forename,surname):
    csvFile = open('bibValues.csv','w')
    for x in range(30):
        bibValue = forename[x][0] + surname[x] + str(ord(location[x][0]))
        csvFile.write(entryID[x] + ',' + bibValue + '\n')
    
    csvFile.close()
    

def main():
    entryID, location, forename, surname, jumps = getData()
    bibGen(entryID,location,forename,surname)
    

main()