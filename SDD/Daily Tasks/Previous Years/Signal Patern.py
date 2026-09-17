def getValid(minNo, maxNo):
    print('Please enter the reading')
    reading = float(input('>'))
    while reading < minNo or reading > maxNo:
        print('The reading should be between', minNo, '&', maxNo)
        print('Please enter the reading')
        reading = float(input('>'))
    
    return reading
    
def main():
    reading = [0.0 for x in range(5)]
    signal = ''
    
    for x in range(5):
        reading[x] = getValid(0,100)
        reading[x] = round(reading[x])
        if reading[x] > 80:
            signal = signal +'S'
        elif reading[x] <30:
            signal = signal + 'P'
        else:
            signal = signal + 'M'
    
    print('Signal Pattern is:', signal)
    
    for x in range(5):
        print('Reading', x+1, '-', reading[x])
        
main()