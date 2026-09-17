# Password program
# Mr Stratton
# 01/10/24

def readSurname(surname):
    txtFile = open('Surname.txt','r')
    for x in range(len(surname)):
        surname[x] = txtFile.readline().strip()
    txtFile.close()
    
    return surname

def createUser(surname, username):
    for x in range(len(surname)):
        username[x] = '2024' + surname[x][:5]
    
    return username  

def createPassword(password):
    import random
    word = ['' for x in range(20)]
    txtFile = open('words.txt','r')
    for x in range(20):
        word[x] = txtFile.readline().strip()
    txtFile.close()
    
    for x in range(20):
        password[x] = word[random.randint(0,19)] + str(random.randint(0,9)) + str(random.randint(0,9))
    
    return password

def writeFile(username, password):
    txtFile = open('passwords.txt','w')
    for x in range(20):
        txtFile.write(username[x] + ' - ' + password[x] + '\n')
    
    txtFile.close()

def main(): # Define
    #0 set up arrays and variables
    surname = ['' for x in range(20)]
    username = ['' for x in range(20)]
    password = ['' for x in range(20)]
    
    #1 Read in surnames 					(out: surname() )
    surname = readSurname(surname) # call
    #2 generate username					(in: surname() out: username() )
    username = createUser(surname, username)
    #3 create password 						(out: password() )
    password = createPassword(password)
    #4 write username and password to file	(in: username(), password() )
    writeFile(username, password) 

main() # sub program call