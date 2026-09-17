# RECORD Person IS { STRING name, INTEGER age }
# DECLARE me INITIALLY Person( "Quintin", 47 )
# DECLARE myAge INITIALLY me.age
# SET me.age TO myAge + 1
#

from dataclasses import dataclass

@dataclass
class person:
    name:str
    age:str

pupilList = [person('',0) for x in range(4)]
print(pupilList)

for x in range(4):
    print('Please enter the name of person',x+1)
    pupilList[x].name = input('>')
    print('What is',pupilList[x].name,'age?')
    pupilList[x].age = int(input('>'))
    
for x in range(4):
    print(pupilList[x].name,pupilList[x].age)