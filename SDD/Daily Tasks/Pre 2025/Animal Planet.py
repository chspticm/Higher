# Animal Planet
# Mr Stratton
# 5/11/24
# Write a program to read the CSV file into an Array of Records.

# 0 set up the record structure
from dataclasses import dataclass

@dataclass
class animal:
    name:str
    species:str
    weight:int
    colour:str

def readCSV(animals):
    csvFile = open('animals.csv','r')
    for x in range(len(animals)):
        a,b,c,d = csvFile.readline().strip().split(',')
        animals[x].name = a
        animals[x].species = b
        animals[x].weight = int(c)
        animals[x].colour = d
    csvFile.close()
    return animals

def display(animals):
    print('Name'.ljust(10),'Species'.ljust(25),'Weight'.ljust(6),'Colour')
    for x in range(len(animals)):
        print(animals[x].name.ljust(10),animals[x].species.ljust(25),str(animals[x].weight).ljust(6),animals[x].colour)

def findMin(animals):
    minPos = 0
    for x in range(1,len(animals)):
        if animals[x].weight < animals[minPos].weight:
            minPos = x
    
    print('The lightest is',animals[minPos].name,animals[minPos].weight)
    
def main():
    # array of animal records
    animals = [animal('','',0,'') for x in range(7)]
    # 1. read the csv file into an array of records
    animals = readCSV(animals)
    # 2. Display the records in a table
    display(animals)
    findMin(animals)

main()