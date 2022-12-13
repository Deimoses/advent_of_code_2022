input = open("day6.txt","r")

instructions = input.read()
input.close()
number = 0
condition = True

while condition:     
   if number+4 <= len(instructions):
        four_chars = instructions[number] + instructions[number + 1] + instructions[number + 2] + instructions[number + 3]
        if not len(set(four_chars)) == len(four_chars):
            number +=1
        else:
            print(number + 4)
            condition = False