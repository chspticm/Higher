# Dice Program
def rolldice(array,size):
    import random
    for x in range(len(array)):
        array[x] = random.randint(1,size)
    
    return array
    
def saveCSV(dice1,dice2,dice3,dice4,dice5,dice6):
    csvFile = open('rolls.csv','w')
    for x in range(len(dice1)):
        csvFile.write(str(dice1[x]) + ',' + str(dice2[x]) + ',' + str(dice3[x]) + ',' + str(dice4[x]) + ',' + str(dice5[x]) + ',' + str(dice6[x]) + '\n')
    csvFile.close()

def check(dice1,dice2,dice3,dice4,dice5,dice6,target):
    found = False
    for x in range(len(dice1)):
        if dice1[x]+dice2[x]+dice3[x]+dice4[x]+dice5[x]+dice6[x] == target:
            found = True
            print(target,'found on roll',x)
    
    if not found:
        print(target,'not found')

def main():    
    dice1 = [0 for x in range(100000)]
    dice2 = [0 for x in range(100000)]
    dice3 = [0 for x in range(100000)]
    dice4 = [0 for x in range(100000)]
    dice5 = [0 for x in range(100000)]
    dice6 = [0 for x in range(100000)]
    
    dice1 = rolldice(dice1,6)
    dice2 = rolldice(dice2,6)
    dice3 = rolldice(dice3,6)
    dice4 = rolldice(dice4,6)
    dice5 = rolldice(dice5,6)
    dice6 = rolldice(dice6,6)
    
    saveCSV(dice1,dice2,dice3,dice4,dice5,dice6)
    check(dice1,dice2,dice3,dice4,dice5,dice6,36)

main()