# Write a program that gets two names and displays them in a message.

def getNames():
    print('Please enter the 1st name')
    nameA = input('>')
    print('Please enter the 2nd name')
    nameB = input('>')
    
    return nameA, nameB

def create(a, b): # Formal Parameter a & b
    message = 'Hello ' + a + ' and ' + b +' enjoy computing!'
    
    return message

def display(message): # Formal Parameter message
    print('+' + '-' * len(message) + '+')
    print('|' + message + '|')
    print('+' + '-' * len(message) + '+')
    
def main():
    #1. get two names   (OUT: name1, name2)
    name1, name2 = getNames()
    #2. create (concatinate) the message (IN: name1, name2 OUT: Message)
    message = create(name1, name2) # Actual Parameter name1, name2 (Arguments)
    #3. display the message (IN: Message)
    display(message) # argument message

main()