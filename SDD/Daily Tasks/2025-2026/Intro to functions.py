# The sum of two number
# Intro to subprograms
# Mr Stratton
# 10/09/25

def get2Numbers():
    #1. get two numbers
    numA = int(input('What is the 1st number? > '))
    numB = int(input('What is the 2nd number? > '))
    return numA, numB

def sumNumbers(numA, numB):
    #2. add the two numbers
    total = numA + numB
    return total

def display(total):
    #3. Display the answer
    print('The total is',total)

def main(): # definition
    numA, numB = get2Numbers()
    total = sumNumbers(numA, numB)
    display(total)

main() # call
