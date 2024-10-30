# Reading from a file

txtFile = open('task1.txt','r')

for x in range(2):
    print(txtFile.readline().strip())

txtFile.close()
print('File closed')
print('How are you\nDoing today?')