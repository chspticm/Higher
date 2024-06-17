#Traversing a 1D array: example 2 (fixed ‘for each’ loop with running total included)
'''
This program is using a loop to access each element of an array, for the purposes of processing the data in the array.
    DECLARE allScores INITIALLY [ 12,34,23,54,32,67,26,23 ]
    DECLARE total INITIALLY 0
    DECLARE counter INITIALLY 0
    FOR EACH FROM allScores DO
        SET total TO total + allScores[counter]
        SET counter TO counter + 1
    END FOR
'''

allScores = [12,34,23,54,32,67,26,23]
total = 0
counter = 0
for score in allScores:
    total = total + allScores[counter]
    counter = counter + 1

print('The sum of the numbers is:', total)