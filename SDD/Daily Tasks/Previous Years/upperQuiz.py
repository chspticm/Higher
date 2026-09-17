def main():
    question = ['Scotland','England']
    answer = ['Edinburgh','London']
    
    for x in range(len(question)):
        print('What is the capital of',question[x])
        uAnswer = input('>')
        if uAnswer.upper() == answer[x].upper() :
            print('Well Done')
        else:
            print('Wrong')
            
main()