# Large Egg Company
# Mr Stratton
# 23/10/24

spaces = 0
print('How many eggs in the order?')
eggs = int(input('>'))

boxes = eggs/25

if boxes != int(boxes):
    boxes += 1
    spaces = 25 - (eggs%25)

print(int(boxes),'boxes required for the eggs')
print('there will be',spaces,'empty spaces')