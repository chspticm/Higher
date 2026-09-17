# Mr Stratton
# Volume
# 29/08/24

def getValidInt(minNo, maxNo):
    print('Please enter a number between', minNo, 'and', maxNo)
    number = int(input('>'))
    while number < minNo or number > maxNo:
        print('The number must be between', minNo, 'and', maxNo)
        print('Please enter a number between', minNo, 'and', maxNo)
        number = int(input('>'))
    
    return number

def main():
    # 1. Get valid length	(Out: Length)
    print('Please enter the length')
    length = getValidInt(1, 100)
    # 2. Get valid breadth	(Out: Breadth)
    print('Please enter the Breadth')
    breadth = getValidInt(1, 100)
    # 3. Get valid height	(Out: Height)
    height = getValidInt(1, 100)
    # 4. Calculate Volume	(In: Length, Breadth, Height Out: Volume)
    # 5. Display Volume		(In: Volume)

main()