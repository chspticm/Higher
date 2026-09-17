# Arrays
# Mr Stratton
# 15/09/25

def get(array):
    for x in range(len(array)):
        array[x] = int(input('Enter Number >'))
    return array

def display(array):
    for x in range(len(array)):
        print(array[x])
        
def main():
    # 0 set up vatiables and arrays
    number = [0 for x in range(5)]
    number = get(number)
    display(number)

main()