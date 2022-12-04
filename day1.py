import re
input = open("day1.txt","r")

def spliter(a):
    regex = r"\n\n"
    return re.split(regex,a.strip())

input_list = spliter(str(input.read()))
result = []

for string in input_list:
    string_list = string.split("\n")
    value = 0
    for number in string_list:
        value += int(number)
    result.append(value)        
print(max(result))

#part two

result.sort(reverse=True)
newlst = result[0:3]
print(sum(newlst))