# SFA Task
# 26/11/25
# Mr Straton

#0. Set up record
from dataclasses import dataclass
@dataclass
class match():
    date:str = ''
    homeTeam:str = ''
    homeScore:int = 0
    awayTeam:str = ''
    awayScore:int = 0
    comp:str = ''
    

def readCSV():
    results = [match() for x in range(33)]
    # 1.1 open file
    csvFile = open('sfa.csv','r')
    # 1.2 read header line
    csvFile.readline()
    # 1.3 for the rest of the file
    for x in range(33):
    # 1.4     read and store the line in the array of records
        a,b,c,d,e,f = csvFile.readline().strip().split(',')
    # 1.5 Next
    csvFile.close()


def main():
    # 1. Read in CSV file (out: match details)
    results = readCSV()
    # 2. Display results (in: match details)

main()