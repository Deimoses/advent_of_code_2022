input = open("day2.txt","r")

instructions = str(input.read())
instructions = instructions.replace(" ","")
instructions = instructions.replace("\n","")
# instruction = "AXCZBY..."

previous_char = ''
count = 0
points = 0

for i in instructions:
    previous_char = instructions[count - 1]
    
    if i == 'X':
        if previous_char == 'A':
            points += 3
        elif previous_char == 'B':
            points += 1
        elif previous_char == 'C':
            points += 2

    if i == 'Y':
        points +=3

        if previous_char == 'A':
            points += 1
        elif previous_char == 'B':
            points += 2
        elif previous_char == 'C':
            points += 3
    
    if i == 'Z':
        points += 6
        
        if previous_char == 'A':
            points +=2
        elif previous_char == 'B':
            points +=3
        elif previous_char == 'C':
            points +=1
    count += 1
print(points)