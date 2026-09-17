# Passage Analyser
# Mr Stratton
# 22/09/25

def getNumber():
    print('How many sentences in the passage')
    number = int(input('>'))
    return number
    
def getSentence():
    print('What is the sentence?')
    string = input('>')
    return string

def countValues(target, string):
    count = 0
    string = string + ' '
    for x in range(len(string)):
        if string[x] == target:
            count += 1
    return count

def findAverage(passage):
    total = 0
    count = 0
    for x in range(len(passage)):
        total = total + passage[x]
        count = count + 1
    
    average = total / count
    
    return average
    
    
def main():
    noSentences = getNumber()
    passage = [0 for x in range(noSentences)]
    
    for x in range(noSentences):
        sentence = getSentence()
        count = countValues(' ',sentence)
        passage[x] = count
    
    average = findAverage(passage)
    print('The average number of words in the passage is',average)  

main()