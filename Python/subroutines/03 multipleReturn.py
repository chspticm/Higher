#

def getDetails():
    print('What is your name?')
    name = input('>')
    print('Where do you stay?')
    address = input('>')
    
    return name, address # sends the contents of the variable back to the caller

def displayDetails(name, address): # function definition - Parameter (name)
    print('Hi I am,', name)
    print('I live in', address)

def main():
    name, address = getDetails()     # function call with assignment
    displayDetails(name, address)    # Function Call - argument Name
    
main()