# prices calculator
# Mr Stratton
# 10/9/25

# Save the 10 prices below into a text file then write a python program to read in the value and display the sum total of the items and average price.

def readFile():
    number = [0.0 for x in range(10)]
    txtFile = open('price.txt','r')
    for x in range(10):
        number[x] = float(txtFile.readline().strip())
    
    return number
    
def calc(array):
    total = 0
    for x in range(len(array)):
        total += array[x]
    
    return total

def avg(array):
    average = calc(array) / len(array)
    return average

def display(total, average):
    print('The total of the prices is',total)
    print('The average of the prices is',round(average,2))
    
def main():
    array = readFile()# 1. read the file
    total = calc(array)# 2. Calcluate total
    average = avg(array)# 3. Calculate the Average
    display(total, average)# 4. Display the answers

main()