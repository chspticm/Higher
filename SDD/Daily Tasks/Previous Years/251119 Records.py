from dataclasses import dataclass

@dataclass
class runner(): # Record Runner
    name:str = ''
    bibNumber:int = 0
    isElite:bool = False

runners = [runner('',0,False) for x in range(5)]

for x in range(5):
    print('Please enter name',x)
    runners[x].name = input('>')

# runner1 = runner('Bob',12,False)
# print(runner1.name)
# runner1.name = input('What is the runners name?')
# print(runner1.name)
# 
# runner2 = runner()
# runner2.name = input('What is the runners name?')
# print(runner2.name)
