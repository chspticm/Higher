print('Writing to file')
textFile = open('Working.txt','w')
textFile.write('Mr Stratton\n')
textFile.write('Works at Coltness High School\n')
for x in range(20):
    textFile.write(str(x+1) + '\n')
textFile.close()
print('File written')