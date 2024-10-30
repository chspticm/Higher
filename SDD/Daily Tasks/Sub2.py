# Basic Subprograms
# Mr Stratton
# 05/09/24

def getDetails():
    print('please enter first number')
    first = int(input('>'))
    print('please enter second number')
    second = int(input('>'))
    
    return first, second
 
def calcTotal(first, second):
    total = first + second
    return total

def display(total):
    print('='*20)
    print('| the total is', total,'|')
    print('='*20)
    
def main():
    first, second = getDetails()   
    total = calcTotal(first, second)
    display(total)
 
main()