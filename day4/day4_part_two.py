import re
input = open("day4.txt","r")

shifts = input.read()
input.close()
shifts = re.split(r',|\n|-',shifts)
shift1 = shifts[0::2]
shift2 = shifts[1::2]
shift1_frist_half = shift1[0::2]
shift1_second_half = shift2[0::2]
shift2_frist_half = shift1[1::2]
shift2_second_half = shift2[1::2]

result = 0
value = 0
condition = True
while condition:
    if value < len(shift1_frist_half):
        shift1_range = list(range(int(shift1_frist_half[value]),int(shift1_second_half[value])+1))
        shift2_range = list(range(int(shift2_frist_half[value]),int(shift2_second_half[value])+1))
        value +=1
        check =  any(item in shift1_range for item in shift2_range)
        check_reverse = any(item in shift2_range for item in shift1_range)
        if check == True or check_reverse == True:
            result +=1
        
    else:
        print(result)
        condition = False