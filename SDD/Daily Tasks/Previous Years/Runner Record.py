from dataclasses import dataclass

@dataclass
class runner:
    name:str = ''
    bibNumber:int = 0
    isElite:bool = False

runner1 = runner() # of type runner
print("runner1 =",runner1)
runner1.name = 'Bob'
runner1.bibNumber = 1
runner1.isElite = False
print("runner1 =",runner1)

runner2 = runner() # of type runner
runner2.name = 'Sue'
runner2.bibNumber = 2
runner2.isElite = True

runner3 = runner('Jane',3,False)



print(runner1.name, runner1.bibNumber, runner1.isElite)
print(runner2.name, runner2.bibNumber, runner2.isElite)
print(runner3.name, runner3.bibNumber, runner3.isElite)

race = [runner() for x in range(5)] # Race array of type runner

for x in range(5):
    print('what is runners name')
    race[x].name = input('>')

for x in range(5):
    print(race[x].name)
