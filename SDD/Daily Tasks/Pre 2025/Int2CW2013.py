# 2013 Int2 CW
# Mr Stratton
# 11/10/24
# Adapted for Higher Class

import locale
locale.setlocale(locale.LC_ALL,'')

def validNo(minNo,maxNo):
    # HINT AREA
    print('Please enter the order number')
    number = int(input('>'))
    while number < minNo or number >maxNo:
        print('The order number must be between',minNo,'and',maxNo)
        print('Please enter the order number')
        number = int(input('>'))
    return number
    
def processOrders(ordNo, totals):
    print('What is the value of order',ordNo,'?')
    value = float(input('>'))
    if ordNo <= 30:
        totals[0] = totals[0] + value
    elif ordNo<=60:
        totals[1] += value
    elif ordNo<=90:
        totals[2] += value
    else:
        print('There is an error with the order Number')
    
    return totals
    
def display(totals):
    print('Group Number'.ljust(15),'Order Value (£)')
    for x in range(3):
        print(str(x+1).ljust(15), locale.currency(totals[x]))

def main():
    # 1.Initialise arrays to set 3 group totals
    totals = [0.0 for x in range(3)]
    # 2.Get the quantity of orders to be processed
    print('How many orders have to be processed?')
    orders = int(input('>'))
    # 3.Loop for quantity of orders
    for x in range(orders):
        # 4.Get a valid order form number
        ordNo = validNo(1,90)
        # 5.Process Orders
        totals = processOrders(ordNo, totals)
    # 6.End loop
    # 7.Display group number and amount raised by group
    display(totals)
    # 8.Calculate and display overall total raised
    overall = totals[0] + totals[1] + totals[2]
    print('The total raised for the project is' + str(locale.currency(overall)))
     
main()