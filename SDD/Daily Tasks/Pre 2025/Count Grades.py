#Create a program that will ask the user for 20 valid grade entries. Grades
#can only be A, B, C, D, and F. The program will have to count how many
#As, Bs, cs, Ds, and Fs were entered. These values should then be
#displayed to the user.

grade = ['' for x in range(5)]
#1 get grades
for x in range(len(grade)):
    print('Please enter grade',x+1)
    grade[x]=input('>')
    while grade[x] != 'A' and grade[x] != 'B' and grade[x] != 'C' and grade[x] != 'D'and grade[x] != 'F':
        print('Only enter ABCDF')
        print('Please enter grade',x+1)
        grade[x]=input('>')

#2 process the grades
totalA = 0
totalB = 0
totalC = 0
totalD = 0
totalF = 0

for x in range(len(grade)):
    if grade[x] == 'A':
        totalA = totalA + 1
    elif grade[x] == 'B':
        totalB = totalB + 1
    elif grade[x] == 'C':
        totalC = totalC + 1
    elif grade[x] == 'D':
        totalD = totalD + 1
    elif grade[x] == 'F':
        totalF = totalF + 1  

#3 display the answer
print('Total A', totalA)