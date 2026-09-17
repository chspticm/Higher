# Local and Global Variables

a = 12 # Global

def display():    
    print(a)
    
def main():
    a = 13 # local
    print(a)
    display()

main()