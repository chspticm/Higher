# Int2 2011 CW

def getAge(name):
    # input validation using AREA  (Ask Repeat Error Ask)
    print('What is',name +'\'s age?') 
    age = int(input('>'))
    while age < 12 or age > 17:
        print('The age must be between 12 and 17')
        print('What is',name +'\'s age?')
        age = int(input('>'))
    
    return age # valid age

def validScore(name,message):
    # input validation using AREA  (Ask Repeat Error Ask)
    print('What is',name +'\'s', message, 'score?')  # allows the score message to be tailored
    score = int(input('>'))
    while score < 0 or score > 50:
        print('The score must be between 0 and 50')
        print('What is',name +'\'s', message, ' score?')
        score = int(input('>'))
    
    return score # valid score

def display(pName, pAge, pScore):
    print("Name".ljust(10), "Age".ljust(10), "Total".ljust(10), "Decision".ljust(10)) # .ljust(10) pads the string to 10 characters
    for x in range(4):
        print(pName[x].ljust(10), str(pAge[x]).ljust(10), str(pScore[x]).ljust(10), end=' ') # str() is used to cast the number to a string so it can be padded. end = ' ' swaps out the crlf for a space 
        if pScore[x] > 70:
            if pAge[x] <= 14:
                print('Accepted to junior orchestra') # is appended to the end of the line
            else:
                print('Accepted to senior orchestra') # is appended to the end of the line
        else:
            print('Declined') # is appended to the end of the line

def main():
    # 0 set up variables
    pName = ['' for x in range(4)]
    pAge = [0 for x in range(4)]
    pScore = [0 for x in range(4)]
    
    # 1 Loop for each pupil
    for x in range(4):
    # 2    Get pupil name
        print("What is the pupil's name?")
        pName[x] = input('>')
    # 3    Get a valid age
        pAge[x] = getAge(pName[x]) 
    # 4    Get two valid scores
        first = validScore(pName[x], 'first')   
        second = validScore(pName[x], 'second')
    # 5    Calculate total score
        pScore[x] = first + second
    # 6 Loop until no more pupils

    # 7 Display results and decision
    display(pName, pAge, pScore)

main()