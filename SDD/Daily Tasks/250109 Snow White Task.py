# Snow White Task
# 9/1/25

'''

0.	Set up Arrays
1.	Get the heights of the 7 dwarves
2.	Set minimum position to 1st position
3.	Loop for other 6 dwarves
4.		If current dwarf shorter than minimum position
5.			Set minimum position to current position
6.		End if
7.	End loop
8.	Display the name of the shortest dwarf

'''

name =['Sneezy','Sleepy','Bashful','Grumpy','Dopey','Doc','Happy']
height=[0 for x in range(7)]

for x in range(7):
    print('What is the height of',name[x])
    height[x] = float(input('>'))

minPos=0
for x in range(1,7):
    if height[x]<height[minPos]:
        minPos = x

print(name[minPos],'is the shortest')
