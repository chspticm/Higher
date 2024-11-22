# Mr Stratton
# 19/11/24
# Higher Functions
                            
def getDetails():
        print('Please enter name')
        return(input('>'))
    

def display(string):
        print(string)

def main():
    name = ['' for x in range(5)]

    for x in range(len(name)):
         name[x] = getDetails() # assign one name at a time to the array

    for x in range(len(name)):
        display(name[x]) # display one name at a time

main()