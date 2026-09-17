# Encrypt Message
# Mr Stratton
# 19/09/25


def encrypt(message):
    print('What is the offset?')
    offset = int(input('>'))
    code = ''
    for letter in message: # for each character
        if ord(letter) >=ord('A') and ord(letter) <= ord('Z'):
            code = code + chr((ord(letter) - ord('A') + offset) % 26 + ord('A'))
        elif ord(letter) >=ord('a') and ord(letter) <= ord('z'):
            code = code + chr((ord(letter) - ord('a') + offset) % 26 +ord('a'))
        else:
            code = code + letter

    return code



def main():
    #1. get a message
    print('What is the message?')
    message = input('>')
    #2. Encrypt the message
    code = encrypt(message)
    #3. display the message
    print(code)

main()