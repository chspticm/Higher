# write a program to read the data from the csv file you created
# forename,surname,year_of_birth,Number_of_papers,Students

from dataclasses import dataclass
@dataclass
class teacher():
    forename:str
    surname:str
    DOB:str
    papers:int
    students:int

def readCSVfile():
    maths = [teacher('','','',0,0) for x in range(20)] # array of records
    
    csvFile = open('maths.txt','r')
    for x in range(20):
        a,b,c,d,e = csvFile.readline().strip().split(',')
        maths[x].forename = a
        maths[x].surname = b
        maths[x].DOB = c
        maths[x].papers = int(d)
        maths[x].students = int(e)
    csvFile.close()
    return maths
    
def average(maths):
    total = 0
    for x in range(20):
        total = total + maths[x].students
    
    return total / 20

def display(maths,average):
    print('The average is',average)
    for x in range(20):
        if maths[x].students < average:
            print(maths[x].forename,maths[x].surname,'has',maths[x].students,'students')

def main():
    maths = readCSVfile()
    avg = average(maths)
    display(maths,avg)

main()