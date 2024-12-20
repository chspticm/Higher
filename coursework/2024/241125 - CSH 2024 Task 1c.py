# CSH Coursework 2024
# Mr Stratton
# 25/11/24

def readFile(company, numEmployees, ceoSalary):
    csvFile = open('companies.csv','r')
    for x in range(100):
        a,b,c = csvFile.readline().strip().split(',')
        company[x] = a
        numEmployees[x] = int(b)
        ceoSalary[x] = int(c)

    csvFile.close()
    return company, numEmployees, ceoSalary

def difference(company, ceoSalary):
    print('Please enter the chosen company\'s name')
    chosen = input('>')
    found = False
    position = findMaxPos(ceoSalary)

def findMaxPos(array):
    maxPos = 0
    for x in range(len(array)):
        pass

def main():
    #0 set up arrays
    company = ['' for x in range(100)]
    numEmployees = [0 for x in range(100)]
    ceoSalary = [0 for x in range(100)]

    #1 Read from file into parallel arrays.  OUT: company(), numEmployees(), ceoSalary() 
    company, numEmployees, ceoSalary = readFile(company, numEmployees, ceoSalary) 
    
    #2 Find and display the difference between the chosen company’s CEO salary and the highest CEO salary.  IN: company(), ceoSalary()   
    difference(company, ceoSalary)
    #3 Find and display the highest number of employees employed by a single company, and the number of companies who employ within 10% of that figure. IN: numEmployees()  
 

main()
