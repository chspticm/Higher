# 2025 Higher Coursework
# 16/1/25

from dataclasses import dataclass
@dataclass
class order():
    orderNum:str = ''
    date:str = ''
    email:str = ''
    option:str = ''
    cost:float = 0.0
    rating:int = 0
        
def readFile():
    orders = [order() for x in range(505)]
    csvFile = open('orders.txt','r')
    for x in range(505):
        a,b,c,d,e,f = csvFile.readline().strip().split(',')
        orders[x].orderNum = a
        orders[x].date = b
        orders[x].email = c
        orders[x].option = d
        orders[x].cost = float(e)
        orders[x].rating = int(f)
        
    csvFile.close()
    return orders
    
def findCust(orders):
    position = -1
    index = 0
    print('Enter the first three letters of the month to search.')
    month = input('>')
    while position == -1 and index < len(orders):
        if orders[index].date[3:6] == month and orders[index].rating == 5:
            position = index
        index +=1
    return position

def writeFile(orders,position):
    txtFile = open('winningCustomer.txt','w')
    if position >= 0:
        txtFile.write(orders[position].orderNum + ',' + orders[position].email + ',' + str(orders[position].cost))
    else:
        txtFile.write('No winner')
        
    txtFile.close()
  
def countOption(orders, target):
    total = 0
    for x in orders:
        if x.option == target:
            total +=1
    return total

def display(orders):
    delivered = countOption(orders,'Delivery')
    collected = countOption(orders,'Collection')
    print('Total number of orders delivered  to date:',delivered)
    print('Total number of orders collected  to date:',collected)

def main():
    
# 1 Read from file into array of records.
    orders = readFile()
# 2 Find the position of the customer who gave the first 5-star rating in a given month.
    position = findCust(orders)
# 3 Write details of the winning customer, or 'no winner' message, to a text file.
    writeFile(orders,position)
# 4 Display the total number of orders delivered and the total number of orders collected.
    display(orders)

main()