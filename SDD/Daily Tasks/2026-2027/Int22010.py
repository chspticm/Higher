# Int 2 2010
# Mr Stratton
# 21/08/26

def getValid():
    print('How many tracks are there?')  # ASK
    tracks = int(input('>'))
    while tracks <1 or tracks >20: # REPEAT
        print('Error, you can only have between 1 and 20 tracks') # ERROR
        print('How many tracks are there?')  # ASK
        tracks = int(input('>'))
    
    return tracks

def getData():
    print('Please enter the title of the track')
    title = input('>')
    print('Please enter the length of the track')
    length = int(input('>'))
    
    return title, length
    
def display(title,length,tracks):
    for counter in range(tracks):
        print(title[counter],'-',length[counter])
        
def main(): # Procedure Decleration
    title = ['' for x in range(20)]
    length = [0 for x in range(20)]
    # 1. Initialise total running time
    total = 0
    # 2. Get valid number of tracks
    tracks = getValid() # Function Call
    # 3. FOR counter = 1 TO number of tracks
    for counter in range(tracks):
    # 4.     Get required data
        title[counter], length[counter] = getData()
    # 5.     Calculate total running time
        total = total + length[counter]
    # 6. NEXT counter 
    # 7. display track titles and track lengths
    display(title,length,tracks)
    # 8. display total running time
    print('The total running time is',total)

main() # procedure call
