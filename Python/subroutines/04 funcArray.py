# Mr Stratton
# 12/06/24
# Higher Functions
                            
def getDetails(array):
    for x in range(len(array)):
        print('Please enter name', x + 1)
        array[x] = input('>')

    return array

def displayArray(array):
    for x in range(len(array)):
        print(array[x])

def main():
    name = ['' for x in range(5)]
    name = getDetails(name)
    displayArray(name)

main()