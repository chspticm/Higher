# Read from file
# Mr Stratton
# 16/9/24

# Reads each line of text one line at a time
# Even if the number of lines is not known

txtFile = open('names.txt','r')

for line in txtFile:
    print(line.strip())

txtFile.close()
# ====================================
# Reads the contents of the file into one
# Massive string

txtFile = open('names.txt','r')
contents = txtFile.read()
txtFile.close()
print(contents)

# ====================================
# Read the contents of a file into an Array
# It is assumed that the file is not longer than 100 lines
name = ['' for x in range(100)]
txtFile = open('names.txt','r')
size = 0

for line in txtFile:
    name[size] = line.strip()
    size += 1

print(name, size)

#======================================
# Read from a file of known size into
# an array of known size

name = ['' for x in range(10)]
txtFile = open('names.txt','r')
for x in range(10):
    name[x] = txtFile.readline().strip()
txtFile.close()
print(name,len(name))