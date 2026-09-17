# Passage Analyser
# Mr Stratton
# 22/09/25
def getSentence():
    print('Please enter the sentence')
    sentence = input('>')
    return sentence

def getNumber():
    print('How many sentences in the passage?')
    number = int(input('>'))
    return number

def countValues(sentence,target):
    total = 0
    for letter in sentence:
        if letter == target:
            total += 1
    return total

def findAverage(passage):
    total = 0
    for number in passage:
        total += number
    
    average = total/len(passage)
    return average

def main():
    number = getNumber()
    passage = [0 for x in range(number)]
    
    for x in range(number):
        sentence = getSentence()
        sentence += ' '
        words = countValues(sentence,' ')
        passage[x] = words
    average = findAverage(passage)
    print('The average number of words in the passage is',average)

main()