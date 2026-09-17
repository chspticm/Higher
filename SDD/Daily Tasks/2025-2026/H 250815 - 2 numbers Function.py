# Mr Stratton
# 15/08/1970
# Introduction - use the program below to
# get two numbers (in a function)
# Display the sum of those numbers in main()

def getNum():
    # refine step 1
    # 1.1 get 1st number
    print('Please enter the 1st number')
    number1 = float(input('>'))
    
    # 1.2 get 2nd number
    print('Please enter the 2nd number')
    number2 = float(input('>'))
    
    return number1, number2

def main():
    
    # main program
    number1, number2 = getNum() # 1. get numbers
    print('The sum us',number1 + number2) # 2. display sum

main()