#Traversing a 1D array: example 1 (fixed loop)
'''
This program is using a loop to access each element of an array, for the purposes of processing the data in the array.
    DECLARE allScores INITIALLY [ 12,34,23,54,32,67,26,23 ]
    FOR counter FROM 0 TO 7 DO
        IF allScores[counter] >= 50 THEN
            SEND “Great Score” & allScores[counter] TO DISPLAY
        END IF
    END FOR
'''

allScores = [12,34,23,54,32,67,26,23]
for counter in range(8):
    if allScores[counter] >= 50:
        print('Great score', allScores[counter])