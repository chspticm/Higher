# 0  Set up Arrays
word = ['' for x in range(20)]
name = ['' for x in range(20)]

# 1 Read words from file
txtFile = open('words.txt','r')
for x in range(20):
    word[x] = txtFile.readline().strip()
    
txtFile.close()

# 2 Read names from file
txtFile = open('surname.txt','r')
for x in range(20):
    name[x] = txtFile.readline().strip()
    
txtFile.close()

# 3 Display words and Names
for x in range(20):
    print(name[x],'-',word[x])