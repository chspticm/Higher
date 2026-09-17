# write user details to file.
# Mr Stratton
# 10/09/26

def writeFile(name,age):
    txtFile = open('details.txt','w')
    txtFile.write(name + ' ' + str(age))
    txtFile.close()
    

def getDetails():
    name = input('please enter your name > ')
    age = int(input('Please enter your age > '))
    return name,age

def main():
    name,age = getDetails()
    writeFile(name,age)

main()