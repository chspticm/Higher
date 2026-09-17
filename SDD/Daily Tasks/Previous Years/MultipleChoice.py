def getInput():
    print('Please enter your answer')
    answer = input('>').upper()
    while answer < 'A' or answer >'E':
        print('Please enter A, B, C, D, or E.')
        answer = input('>').upper()
    
    return answer

def main():
    
    print(getInput())

main()