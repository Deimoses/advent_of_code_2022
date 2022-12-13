import re
input = open("day5.txt","r")

instructions = str(input.read())
input.close()

move_instructions = instructions.split("\n") and instructions.split('move', 1)[1]
move_instructions = move_instructions.replace("move","")
move_instructions = move_instructions.replace("to","")
move_instructions = move_instructions.replace("from","")
move_instructions = move_instructions.replace(" ","")
move_instructions = move_instructions.split("\n")
instructions = instructions.split("\n")
to_be_move = []
collum_number = []
finish_collum = []
collum1 = []
collum2 = []
collum3 = []
collums = [collum1,collum2,collum3]
number_of_instruction = 0
condition = True
for x in move_instructions:
    to_be_move.append(x[0])
    collum_number.append(x[1])
    finish_collum.append(x[2])

for x in instructions:
    for i in x:
        if i.isupper():
            if i == x[1]:
                collum1.append(i)
            elif i == x[5]:
                collum2.append(i)
            elif i == x[9]:
                collum3.append(i)

while condition:
    if number_of_instruction < len(to_be_move):
        
        for i in collum_number:
            x=collums[int(i)-1]
            if finish_collum[number_of_instruction] == 2:
                collum2.insert(0,x[int(to_be_move[number_of_instruction])-1 ])
                x.remove(int(to_be_move[number_of_instruction])-1)
            elif finish_collum[number_of_instruction] == 3:
                collum3.insert(0,x[int(to_be_move[number_of_instruction])-1 ])
                x.remove(int(to_be_move[number_of_instruction])-1)
            
            if int(finish_collum[number_of_instruction]) == 1:
                collum1.insert(0,collum1[int(to_be_move[number_of_instruction])-1 ])
                collum2.remove(collum2[int(to_be_move[number_of_instruction])-1])
            elif int(finish_collum[number_of_instruction])== 3:
                collum3.insert(0,collum1[int(to_be_move[number_of_instruction])-1 ])
                collum2.remove(collum2[int(to_be_move[number_of_instruction])-1])
            if int(finish_collum[number_of_instruction]) == 2:
                collum2.insert(0,collum1[int(to_be_move[number_of_instruction])-1 ])
                collum3.remove(collum3[int(to_be_move[number_of_instruction])-1])
            elif int(finish_collum[number_of_instruction]) == 1:
                collum1.insert(0,collum1[int(to_be_move[number_of_instruction])-1 ])
                collum3.remove(collum3[int(to_be_move[number_of_instruction])-1])
        number_of_instruction +=1
        print(number_of_instruction)
    else:
        print(collum1[0],collum2[0],collum3[0])
        condition = False