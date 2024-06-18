# Running total within a loop: example 1 (fixed loop)
'''
This program is used to calculate the sum of a known number of values entered by the user one at a time.
    DECLARE total INITIALLY 0
    FOR loop FROM 1 TO 10 DO
        RECEIVE number FROM KEYBOARD
        SET total TO total + number
    END FOR
'''

total = 0
for loop in range(10):
    print('Please enter a number')
    number = int(input('>'))
    total = total + number

print('The total is:', total)