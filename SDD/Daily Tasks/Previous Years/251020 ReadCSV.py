# 0. Set up records and variables
from dataclasses import dataclass
@dataclass
class game():
    name:str = ''
    pegi:str = ''
    publisher:str = ''
    date: str = ''
    year: int = 0
    
def readCSV():
    # 1.0 set up array of records
    games = [game('','','','',0) for x in range(12)]
    # 1.1 open the file
    csvFile = open('games.csv','r')
    # 1.2 loop for the 12 lines
    for x in range(12):
        # 1.3     read the line
        line = csvFile.readline().strip()
        # 1.4     split the line
        a,b,c,d,e = line.split(',')
        # 1.5     store in array of records
        games[x].name = a
        games[x].pegi = b
        games[x].publisher = c
        games[x].date = d
        games[x].year = int(e)
    # 1.6 close the file
    csvFile.close()
    return games

def display(games):
    print('Name'.ljust(30),'Publisher'.ljust(26),'Pegi')
    for x in range(len(games)):
        if games[x].year == 2024:
            print(games[x].name.ljust(30),games[x].publisher.ljust(26),games[x].pegi)

def main():
    # 1. Read in the contents of the file
    games = readCSV()
    # 2. Display the file contents in a table
    display(games)


main()