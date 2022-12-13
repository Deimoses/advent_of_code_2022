input = open("day3.txt","r")
lst = str(input.read())
input.close()
lst = lst.split("\n")
match_in_word = ''
match = []
value = 0
number = 0
number1 = lst[0::3]
number2 = lst[1::3]
number3 = lst[2::3]

condition = True
while condition:
    if number < len(number1):
        for char1 in number1[number]:
            for char2 in number2[number]:
                for char3 in number3[number]:
                    if char1 == char2 and char1 == char3:
                        match_in_word = char1
        number +=1
        match.append(match_in_word)
    else:
        condition = False


for i in match:
    if i.isupper():
        value += ord(i) - 38
    else:
         value += ord(i) - 96
print(value)