from dataclasses import dataclass
@dataclass
class result():
    date:str = ''
    hTeam:str = ''
    hScore:int = 0
    aTeam:str = ''
    aScore:int = 0
    comp:str = ''
 
def readcsv():
    results = [result() for x in range(33)]
    csvFile = open('sfa.csv','r')
    csvFile.readline() # skip 1st line
    for x in range(33):
        a,b,c,d,e,f = csvFile.readline().strip().split(',')
        results[x].date = a
        results[x].hTeam = b
        results[x].hScore = int(c)
        results[x].aTeam = d
        results[x].aScore = int(e)
        results[x].comp = f
        
    csvFile.close()
    return results

def display(results):
    for x in range(len(results)):
        match = 'Draw'
        if results[x].hScore > results[x].aScore:
            match = 'Home Win'
        elif results[x].hScore < results[x].aScore:
            match = 'Away Win'
            
        print(match,results[x].hTeam,results[x].hScore,':',results[x].aScore,results[x].aTeam)
    
def main():
    results = readcsv()
    display(results)

main()