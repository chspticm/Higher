# Read a CSV file into an Array of records
# and display the contents

from dataclasses import dataclass
@dataclass

class book():
    title:str
    author:str

def readCSV():
    books = [book('','') for x in range(10)]
    CSVfile = open('books.csv','r')
    for x in range(10):
        a,b = CSVfile.readline().strip().split(',')
        books[x].title = a
        books[x].author = b
    
    CSVfile.close()
    return books

def longest(books):
    maxTitle = len(books[0].title)
    maxAuthor = len(books[0].author)
    for x in range(1,len(books)):
        if len(books[x].author) > maxAuthor:
            maxAuthor = len(books[x].author)
        if len(books[x].title) > maxTitle:
            maxTitle = len(books[x].title)
    
    return maxTitle, maxAuthor

def display(books):
    maxTitle, maxAuthor = longest(books)
    print('|' + "Author(s)".ljust(maxAuthor) + '|' + "Title".ljust(maxTitle) + '|')
    print('+'+ '-' * maxAuthor +'+' + '-' * maxTitle + '+')
    for x in range(10):
        print('|' + books[x].author.ljust(maxAuthor) + '|' + books[x].title.ljust(maxTitle) + '|')
        
def main():
    #1 read in the file
    books = readCSV()
    #2 display the array
    display(books)
    
main()
    
