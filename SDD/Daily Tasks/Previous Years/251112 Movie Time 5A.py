print('Please enter the movie run time in minutes')
minutes = int(input('>'))

hours = int(minutes/60)
remaining = minutes % 60

print(minutes,'minutes is', hours, 'hours and',remaining,'minutes')