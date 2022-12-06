input = open("day6.txt","r")

instructions = input.read()
number = 0
condition = True

while condition:     
   if number+14 <= len(instructions):
        four_chars = instructions[number] + instructions[number + 1] + instructions[number + 2] + instructions[number + 3] + instructions[number + 4] + instructions[number + 5] + instructions[number + 6] + instructions[number + 7] + instructions[number + 8] + instructions[number + 9] + instructions[number + 10] + instructions[number + 11] + instructions[number + 12] + instructions[number + 13]
        if not len(set(four_chars)) == len(four_chars):
            number +=1
        else:
            print(number +14)
            condition = False