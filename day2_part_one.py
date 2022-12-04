input = open("day2.txt","r")

instructions = str(input.read())

instructions = instructions.replace(" ","")
instructions = instructions.replace("\n","")
# instruction = "AXCZBY..."

count = 0
points = 0
previous_char = ''
for i in instructions:
    previous_char = instructions[count - 1]
    if i == 'Y':
        points += 2
    elif i == 'X':
        points += 1
    elif i == 'Z':
        points += 3
    if previous_char == 'A' and i == 'Y':
        points += 6
    elif previous_char == 'A' and i == 'X':
        points += 3 
        
    if previous_char == 'B' and i == 'Z':
        points += 6
    elif previous_char == 'B' and i == 'Y':
        points += 3
        
    if previous_char == 'C' and i == 'Z':
        points += 3
    elif previous_char == 'C' and i == 'X':
        points +=  6
    count += 1
print(points)