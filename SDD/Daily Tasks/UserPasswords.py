# Generate usernames and password
# Mr Stratton
# 23/09/24

def createPassword(password): # FROM OTHER CLASS NEEDS FIXED
    import random
    txtFile = open('words.txt','r')
    word = ['' for x in range(20)]
    for x in range(20):
        word[x] = txtFile.readline().strip()
    txtFile.close()

    for x in range(20):
        password[x] = word[random.randint(0,19)] + str(random.randint(0,9)) + str(random.randint(0,9))
    
    return password


def readFile(surname, randWord):
    txtFile = open('surname.txt','r')
    for x in range(20):
        surname[x] = txtFile.readline().strip()
    txtFile.close()
    
    txtFile = open('words.txt','r')
    for x in range(20):
        randWord[x] = txtFile.readline().strip()
    txtFile.close()
    
    return surname, randWord


def main():
    surname = ['' for x in range(20)]
    randWord = ['' for x in range(20)]
    password = ['' for x in range(20)]
    username = ['' for x in range(20)]
    
    # 1. Read in surname and word files (out: surname(), word())
    surname, randWord = readFile(surname, randWord)
  
    # 2. Generate username (in: surname(), out: Username() )
    # 3. Generate password (in: word(), out: Password() )
    # 4. Write to file (in Password(), Username() )
    

main()
