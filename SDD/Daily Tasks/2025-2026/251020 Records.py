from dataclasses import dataclass
@dataclass
class runner():
    name:str
    bibNumber:int
    elite:bool

runner1 = runner('Bob',12,False)
runner2 = runner('Sue',1,True)

print(runner1.name)
print(runner2.name)