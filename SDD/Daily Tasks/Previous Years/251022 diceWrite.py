def rollDice():
    import random
    dice =[random.randint(1,20) for x in range(1000)]
    return dice

def saveData(dice):
    txtFile = open('rolls.txt','w')
    for x in range(len(dice)):
        txtFile.write(str(dice[x]) + '\n')
    txtFile.close()

def main():
    dice = rollDice()
    saveData(dice)

main()