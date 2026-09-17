
def getNumbers():
    a = float(input('Please enter the 1st number > '))
    b = float(input('Please enter the 2nd number > '))
    return a,b

def sumNumbers(a,b):
    total = a + b
    return total

def displayNumbers(a,b,total):
    print('the total of',a,'+',b,'is',total)

def main():
    a,b = getNumbers()
    total = sumNumbers(a,b)
    displayNumbers(a,b,total)

main()