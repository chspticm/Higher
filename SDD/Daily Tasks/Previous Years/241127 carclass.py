from dataclasses import dataclass
@dataclass
class details:
    make:str
    model:str
    engSize:float
    doors:int

print('Correct way - all elements of array are different')
cars = [details('','',0.0,0) for x in range(5)]
print(cars)
cars[0].make = 'Ford'
print('Car 0',cars[0].make)
print('Car 1',cars[1].make)
print(cars)

print('\n'*3)

print('Wrong way - all elements of array are same element')
cars = [details for x in range(5)]
print(cars)
cars[0].make = 'Ford'
print('Car 0',cars[0].make)
print('Car 1',cars[1].make)
print(cars)