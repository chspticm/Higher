# Program displays the users name with stars
                            
def getDetails():
    print('Please enter your name')
    name = input('>') # local variable
    return name

def displayStars(name):
    print('*****',name,'*****')

def main():
    name = getDetails()     # call the function getDetails and assign the result to name
    displayStars(name)      # call display with the argument name

main()