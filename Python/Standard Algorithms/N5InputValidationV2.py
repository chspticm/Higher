# Input validation: example 2 (until loop)

'''This program is used to obtain a value between 10 and 20 inclusive.
    REPEAT
        RECEIVE number FROM KEYBOARD
        IF number < 10 OR number > 20 THEN
            SEND “Error, please enter again” TO DISPLAY
        END IF
    LOOP UNTIL number >= 10 AND number <= 20
'''

while True:
    print('Please enter a number')
    number = int(input('>'))
    if number < 10 or number > 20:
        print('Error, please enter again')
    else:
        break

print('Valid number between 10 and 20:', number)