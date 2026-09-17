def countOcc(array, target):
    count = 0

    for x in range(len(array)):
        if array[x] == target:
            count = count + 1
    
    return count

def main():
    numbers = [23, 76, 50, 71, 98, 23, 50, 37, 93, 71, 37, 40, 21, 50]
    target = 50
    total = countOcc(numbers,target)
    print('The value',target,'appears',total,'times in the array')
    
main()
