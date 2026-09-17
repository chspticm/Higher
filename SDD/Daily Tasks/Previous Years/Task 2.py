# Task 2
#  Mr Stratton
# 15/09/2025

def get():
    print('How many sentences in the passage?')
    number = int(input('>'))
    return number

def main():
    passage = [0 for x in range(10)] # Assume only 10 sentences
    noOfSent = get()
    for x in range(noOfSent):
        sentence = getSent()
        words = count(sentence)
        passage[x] = words
    average = calc(passage)
    display(average)

main()