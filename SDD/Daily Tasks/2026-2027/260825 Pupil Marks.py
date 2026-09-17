# Task 1d
# Mr Stratton
# 25/08/26

def getDetails():
    names = ['' for x in range(5)]
    marks = [0 for x in range(5)]
    for x in range(len(names)):
        names[x] = input('Please enter the pupils name >')
        marks[x] = int(input('Please enter ' + names[x] + '\'s mark >'))
    
    return names, marks

def main():
    # 1. get names and marks
    names,marks = getDetails()
    # 2. find highest mark
    maxMark = findMax(marks)
    # 3. find lowest mark
    # 4. display pupils with these marks

main()