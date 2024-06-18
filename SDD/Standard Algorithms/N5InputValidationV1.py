# N5 Input validation: example 1 (while loop)
'''
This program is used to obtain a value between 10 and 20 inclusive.
    RECEIVE number FROM KEYBOARD
    WHILE number < 10 OR number > 20 DO
        SEND “Error, please enter again” TO DISPLAY
        RECEIVE number FROM KEYBOARD
    END WHILE
'''

print('Please enter a number')
number = int(input('>'))
while number < 10 or number > 20:
    print('Error, please try again')
    print('Please enter a number')
    number = int(input('>'))

print('Valid number between 10 and 20:', number)