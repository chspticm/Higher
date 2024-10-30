def calcGrade(score):
    grade = ['' for x in range(5)]
    for x in range(len(score)):
        if score[x] >= 85:
            grade[x] = 'A'
        elif score[x] >= 70:
            grade[x] = 'B'
        elif score[x] >= 55:
            grade[x] = 'C'
        elif score[x] >= 40:
            grade[x] = 'D'
        else:
            grade[x] = 'Fail'
    
    return grade

def display(array1, array2, array3):
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    print(RED + 'Computing Grades' + END)
    print(BOLD + 'Name'.ljust(10) + 'Score'.ljust(10) + 'Grade'.ljust(10) + END)
    for x in range(len(array1)):
        print(array1[x].ljust(10) + str(array2[x]).ljust(10) + array3[x].ljust(10))
        

def main():
    name = ['Bob','Sue','Jane','Frank','John']
    score = [50,60,70,40,65]
    
    # 1. Calculate the grades 	(In: score() Out:grade())
    grade = calcGrade(score)

    # 2. display the grades		(In: name(), score(), grade() )
    display(name,score,grade)
main()