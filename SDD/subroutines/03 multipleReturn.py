#

def getDetails():
    print('What is your name?')
    name = input('>') # local variable
    print('Where do you stay?')
    address = input('>') # local variable
    
    return name, address # sends the contents of the variable back to the caller

def displayDetails(name, address): # function definition - Parameter (name)
    print('Hi I am,', name)
    print('I live in', address)

def main():
    name, address = getDetails()     # function call with assignment
    displayDetails(name, address)    # Function Call - arguments Name & address
    
main()