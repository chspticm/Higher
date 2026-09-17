'''
[x] Read the attached file into an Array of records
[X] Check that the line total is correct for all items. You can test this by changing the price or line total in the CSV file.
[X] How many items in total were purchased?
[X] What was the total price of the weekly shop?
[] What was the average price per item?
[] Display the category and item, without the part in the brackets. i.e. Meat - Chicken Breast
[] Ask the user for a category and display all items in that category.
'''
from dataclasses import dataclass
@dataclass
class item():
    name:str
    qty:int
    price:float
    total:float
    cat:str

def readCSV():
    # it is assumed that there are 50 items and are all valid
    receipt = [item('',0,0.0,0.0,'') for x in range(50)]
    csvFile = open('receipt.csv','r')
    csvFile.readline() # ignore the header
    for x in range(50):
        line = csvFile.readline().strip()
        a,b,c,d,e = line.split(',')
        receipt[x].name = a
        receipt[x].qty = int(b)
        receipt[x].price = float(c)
        receipt[x].total = float(d)
        receipt[x].cat = e
        
    csvFile.close()
    return receipt

def checkTotal(receipt):
    correct = True
    for x in range(len(receipt)):
        if receipt[x].total != receipt[x].price * receipt[x].qty:
            correct = False
            print(receipt[x].name,'Not correct')
            
    if not correct:
        print('line totals not correct')
    else:
        print('line totals are correct')
            
def totalPrice(receipt):
    total = 0
    for x in range(len(receipt)):
        total += receipt[x].total
    
    print('The total for the shop was £',total)
        

def main():
    receipt = readCSV()
    checkTotal(receipt)
    print(len(receipt),'items were purchased')
    totalPrice(receipt)

main()