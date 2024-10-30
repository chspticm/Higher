# School Marks
# Mr Stratton
# 13/9

name = ['' for x in range(4)]
mark = [0 for x in range(4)]
grade = ['' for x in range(4)]

for x in range(4):
    print('What is the name of pupil',x+1,'>')
    name[x] = input('>')

for x in range(4):
    print('What is the mark for pupil',name[x],'>')
    mark[x] = int(input('>'))

for x in range(4):
    if mark[x]>= 75:
        grade[x] = 'A'
    elif mark[x]>= 60:
        grade[x] = 'B'
    elif mark[x]>= 50:
        grade[x] = 'C'
    elif mark[x]>= 40:
        grade[x] = 'D'
    else:
        grade[x] = 'Fail'

for x in range(4):
    print(name[x],mark[x],grade[x])
    