# Quiz Program
# Mr Stratton
# 11/03/26

# CSV format category, question,correct, wrong1, wrong2, wrong3

from dataclasses import dataclass
@dataclass
class rQuestion:
    category:str
    question:str
    correct:str
    wrong1:str
    wrong2:str
    wrong3:str
    
class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    
def readCSV():
    questions = []
    CSVfile = open('quizQuestions.csv','r')
    CSVfile.readline() # skip headers
    for line in CSVfile:
        category,question,correct,wrong1,wrong2,wrong3 = line.strip().split(',')
        questions.append(rQuestion(category,question,correct,wrong1,wrong2,wrong3))
    CSVfile.close()
    return questions

def ask(question):
    import random
    correct = False
    print('Category:',question.category) # Change to colour change function
    print('What is',question.question,'?')
    
    #Display answers in random order
    ansList = [question.correct,question.wrong1,question.wrong2,question.wrong3]
    shuffledList = random.sample(ansList,len(ansList))
    for x in range(len(shuffledList)):
        print(chr(65+x),'-',shuffledList[x])
    
    answer = input('>').upper()
    #Check answer
    if shuffledList[ord(answer)-65] == question.correct:
        correct = True

    return correct
    


def main():
    score = 0
    questions = readCSV()
    for question in questions:
        correct = ask(question)
        if correct:
            score+=1
        
    print(Colors.GREEN + 'Your Score was:',score)

main()