# Local variables in subroutines

def displayName():
    print('What is your name?')
    name=input('>') # Local Variable
    print('Hi there,',name)
    
def main():
    name="John"
    displayName() # Function Call
    print(name)   

main()