# Write a program to display the area of a circle for a given radius area = pi*r**2

# 1. get radius
# 2. calculate Area
# 3. Display Area

def getRad():
    print('What is the radius')
    rad = float(input('>'))
    return rad

def calcArea(radius):
    area = 3.14 * radius**2
    return area

def display(radius, area):
    print('The area of the circle with the radius',radius,'is',area)
    
def main():
    radius = getRad()
    area = calcArea(radius)
    display(radius, area)
    
main()