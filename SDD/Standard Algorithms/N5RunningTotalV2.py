# Running total within a loop: example 2 (conditional loop)
'''
This program is used to calculate the sum of an unknown number of values entered by the user one at a time.
    DECLARE total INITIALLY 0
    REPEAT
        RECEIVE number FROM KEYBOARD
        SET total TO total + number
        SEND “Do you wish to enter another value” TO DISPLAY
        RECEIVE choice FROM KEYBOARD
    LOOP UNTIL choice = ”no”
'''

total = 0
while True:
    print('Please enter a number')
    number = int(input('>'))
    total = total + number
    print('Do you wish to enter another value?')
    choice = input('>')
    if choice == 'no':
        break

print('The sum of the numbers is:', total)