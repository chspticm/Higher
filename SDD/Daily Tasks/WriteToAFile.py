# write to a file
# Mr Stratton
# 20/9/24

# Ask for persons Name & Age and write to a file

print('What is your name?')
name = input('>')
print('What is your age?')
age = int(input('>'))

txtFile = open('Task1.txt','a')
txtFile.write(name + ' - '  + str(age) + '\n')

txtFile.close()