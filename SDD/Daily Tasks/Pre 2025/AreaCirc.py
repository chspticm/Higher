# Area of a circle
# Mr Stratton
# 08/10/24

def getRadius(): # Definition, where we define the sub program
    # Function
    print('What is the radius?"')
    rad = float(input('>'))
    return rad

def calcA(r):# r is a formal parameter
    # Function
    a = 3.14 * r**2
    return a

def display(area, radius):
    print('The area of a circle with the radius', radius)
    print('Is',area)
    
    
def main():
    # 1. Get the radius (out: radius)
    radius = getRadius() # function call
    # 2. Calculate the area (in: Radius Out: Area)
    area = calcA(radius) # actual parameter radius
    # 3. Display the area # (in: area, radius)
    display(area, radius) 
    
main()