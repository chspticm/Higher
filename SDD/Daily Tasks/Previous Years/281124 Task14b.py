# Task 14b: A class has 5 students, the program must take in 5 names (stored in an
# array) and then take in 5 test scores (also stored in an array). The test is out of I ff)
# and all scores should be validated. The pass mark is 70%. The program should then
# display a list of who has passed and who has failed.
# Extension: Can you make the grading more complex? Please refer to task 70.

# 0. Set up Arrays and Variables Name
name = ['' for x in range(5)]
score = [0 for x in range(5)]
# 1. Get 5 Names
for x in range(5):
    print('What is the name?')
    name[x] = input('>')
# 2. Get 5 Test Scores
for x in range(5):
    print('What is the test score for', name[x])
    score[x] = int(input('>'))
    while score[x] < 0 or score[x] > 150:
        print('Error, score is between 0 and 150')
        print('What is the test score for', name[x])
        score[x] = int(input('>'))
# 3. Display who has passed
print('The following pupils have passed')
for x in range(5):
    if score[x] >= (150*0.7):
        print(name[x])
# 4. Display who has failed