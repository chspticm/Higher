def getDetails():
    # Get details from user
    print('Please enter first number')
    first = int(input('>'))
    print('Please enter second number')
    second = int(input('>'))
    print('Please enter third number')
    third = int(input('>'))
    
    return first, second, third

def calcTotal(first, second, third):
    # Calculte the total
    total = first + second + third
    return total

def dispTotal(first, second, third, total):
    # Display the total
    print('The total of', first, '+', second, '+', third, 'is', total)
    
first, second, third = getDetails()
total = calcTotal(first, second, third)
dispTotal(first, second, third, total)