from dataclasses import dataclass

@dataclass
class feature:
    brand:str 
    refNo:str
    load:int
    spin:int
    price:float 
    stock:int 
    
machines = [feature('','',0,0,0.0,0) for x in range(80)]       