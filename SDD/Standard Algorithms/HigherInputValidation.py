def getValidInt(minNo, maxNo):
    # Input validation with error handling for incorrect data types
    while True:
        try: # Trap any error
            print('Please enter a number between',minNo,'and',maxNo)
            number = int(input('>')) # change here to hand other data types
            if number < minNo or number > maxNo:
                print('Error, the number must be between',minNo,'and',maxNo)
            else:
                return number # early return of valid integer
        except ValueError: # Execute on wrong data type
            print('Make sure you are entering a whole number')

print('A valid number is', getValidInt(1,20)) # call with min and max integer values