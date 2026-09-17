from dataclasses import dataclass

@dataclass
class pupil:
    name:str
    dayDOB:int
    monthDOB:int
    yearDOB:int
    
pupil1 =pupil('Bob',1,1,1980)
class5A = [pupil('',0,0,0) for x in range(20)]
