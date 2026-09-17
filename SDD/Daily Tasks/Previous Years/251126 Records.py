from dataclasses import dataclass

@dataclass
class period():
    number:int = 0
    date:str = ''
    name:str = ''
    teacher:str = ''
    time:str = ''
    topic:str = ''

period3 = period(3,'26/11','Higher Computing','Mr Stratton','10:50','Records')

print(period3.name,period3.topic)

periods = [period() for x in range(32)]