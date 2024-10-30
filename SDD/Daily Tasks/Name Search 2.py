# Create a program that asks the user to type in 10 names.
# The program will then ask the user to type in a name they
# would like to search for. The program should then display
# the position of that name within the array.

name = [ '' for x in range(10)]
for x in range(len(name)):
    print('please enter name',x+1)
    name[x] = input('>')

print('What is the target name')
target = input('>')

for x in range(len(name)):
    if target == name[x]:
        print(target,'found at position',x)