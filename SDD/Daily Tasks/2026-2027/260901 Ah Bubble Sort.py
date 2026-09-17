def bubbleSort(array): # PROCEDURE bubble_sort(list) 
    n = len(array) # DECLARE n INITIALLY length(list) 
    swapped = True # DECLARE swapped INITIALLY TRUE 
    while swapped and n >=0: # WHILE swapped AND n >= 0 
        swapped = False # SET swapped TO False 
        for i in range(n-1): # FOR i = 0 to n-2 DO 
            if array[i] > array[i+1]: # IF list[i] > list[i+1] THEN
                temp = array[i] # SET temp TO list[i]
                array[i] = array[i+1] # SET list[i] TO list[i+1]
                array [i+1] = temp # SET list[i+1] TO temp 
                swapped = True # SET swapped TO TRUE
                print(array)
            # END IF 
        # END FOR 
        n = n-1# SET n TO n - 1 
    # END WHILE 
# END PROCEDURE

def main():
    import random
    # array = [random.randint(1,1000) for x in range(10)]
    array = [5,1,4,2,8,9]
    print(array)
    bubbleSort(array)
    print(array)
    
main()
