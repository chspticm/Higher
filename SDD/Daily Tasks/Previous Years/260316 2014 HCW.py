# 2013-2014 Higher CW Task
# Mr Stratton
# 16/03/26

def getValid(minNo,maxNo):
    while True:
        print('Please enter the number')
        number = int(input('>'))
        if number < minNo or number > maxNo:
            print('Error! number must be between',minNo,'and',maxNo)
        else:
            return number

def getData():
    print('Please enter the customer\'s name')
    name = input('>')
    
    print('Please enter',name,'phone number')
    telNo=input('>')
    while len(telNo) != 11:
        print('The Telephone nummber must have 11 characters')
        print('Please enter',name,'phone number')
        telNo=input('>')
    
    print('Please enter the group size')
    group = getValid(1,20)
    
    print('Please enter the rating')
    rating = getValid(1,10)
    
    return name, telNo, group, rating
    
def getYN():
    while True:
        answer = input('>')
        if answer == 'Y' or answer == 'y':
            return False
        elif answer == 'N' or answer == 'n':
            return True
        else:
            print('Please enter Y or N')
        
def largestGroup(group,size):
    biggest = group[0]
    for x in range(1,size+1):
        if group[x] > biggest:
            biggest = group[x]
    
    print('The largest group tonight was:',biggest)
  
def displayMeals(rated,size):
    poor = 0
    good = 0
    excellent = 0
    for x in range(size+1):
        if rated[x] <= 3:
            poor += 1
        elif rated[x] <=6:
            good += 1
        else:
            excellent += 1
    
    print('The customers rated tonight\'s meals as:')
    print('Poor:',poor)
    print('Good:',good)
    print('Excellent',excellent)
    
def main():
    name = ['' for x in range(20)]
    telNo = ['' for x in range(20)]
    group  = [0 for x in range(20)]
    rating = [0 for x in range(20)]
    size = 0
    while True:
        name[size],telNo[size],group[size],rating[size] = getData()
        print('Do you want to enter further questionnaire data (Y/N)')
        if getYN():
            break
        else:
            size += 1
            
    largestGroup(group,size)
    displayMeals(rated,size)
    displayGroups()

main()