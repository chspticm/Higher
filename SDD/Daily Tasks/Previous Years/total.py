# Total v1
# Mr Stratton
# 19/08/24

# Write a program to add two numbers together.

def getNumbers(numbers):
    for x in range(len(numbers)):
        print('Please enter the number', x + 1)
        numbers[x] = float(input('>'))
    
    return numbers
    
def totalNumbers(numbers):
    total = 0
    for x in range(len(numbers)):
        total = total + numbers[x]
    
    return total

def displayNumbers(numbers, total):
    print('the total of', numbers)
    print('is', total)

def main():
    numbers = [0.0 for x in range(10)]	#0. set up array
    
    numbers = getNumbers(numbers)		#1. Get two numbers
    total = totalNumbers(numbers)		#2. Add numbers together
    displayNumbers(numbers, total)		#3. Display the total

main()