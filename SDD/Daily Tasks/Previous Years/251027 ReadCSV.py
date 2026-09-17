# read CSV File
# Mr Stratton
# 27/10/25

def readCSV():
    author = ['' for x in range(10)]
    title = ['' for x in range(10)]
    csvFile = open('books.csv','r')
    for x in range(10):
        line = csvFile.readline().strip() # remove the line break
        a,b = line.split(',') # Split the string at the comma
        
        title[x] = a
        author[x] = b
    
    csvFile.close()
    
    return title,author

def display(title,author):
    for x in range(10):
        print(title[x].ljust(45),author[x])

def main():
    title, author = readCSV()
    display(title,author)

main()