numbers = [12,4,43,54,3,23,6,87,5,4,98,90]

largest = numbers[0]			#1. Set maximum to 1st item in array
for x in range(1,len(numbers)):	#2. Loop for all other items in array
    if numbers[x] > largest:	#3.		if current item greater than maximum
        largest = numbers[x]	#4.			Set maximum to current item

print('The Largest number is',largest)