def getNames():
    name = ['' for x in range(5)]
    for x in range(5):
        print('What is pupil',x + 1,'name')
        name[x] = input('>')
    
    return name

def getMarks(name):
    mark = [0 for x in range(5)]
    for x in range(5):
        print('What mark did',name[x],'get?')
        mark[x] = int(input('>'))
        
    return mark


def findMaxPos(array):
    maxPos = 0
    for x in range(1,len(array)):
        if array[x] > array[maxPos]:
            maxPos = x
    
    return maxPos

def main():
    name = getNames() # get 5 names
    mark = getMarks(name) # get 5 marks
    maxPos = findMaxPos(mark) # find the largest mark
    print(name[maxPos], 'has the largest mark of',mark[maxPos]) # Display largest mark and name
    
main()