def insertionSort(array): # PROCEDURE insertion_sort(list)
    value = 0 # DECLARE value INITIALLY 0 
    index = 0 # DECLARE index INITIALLY 0
    for i in range(1,len(array)): # FOR i = 1 to length(list)-1 DO
        value = array[i] # SET value TO list[i]
        index = i # SET index TO i
        while (index > 0) and (value < array[index-1]): # WHILE (index > 0) AND (value < list[index-1]) DO
            array[index] = array[index-1] # SET list[index] TO list[index-1]
            index = index - 1 # SET index TO index - 1 
        # END WHILE
        array[index] = value # SET list[index] TO value
    # END FOR 
    return array # END PROCEDURE
    
def main():
    import random
    # array = [random.randint(1,1000) for x in range(10)]
    array = [9,8,7,6,5]
    print(array)
    insertionSort(array)
    print(array)
    
main()
