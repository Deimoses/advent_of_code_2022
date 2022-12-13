input = open("day3.txt","r")
lst = str(input.read())
input.close()
lst = lst.split("\n")
match_in_word = ''
match = []
value = 0
for i in lst:
    number = len(i)//2
    frist_rucksacks = i[0:number]
    second_rucksacks = i[number:]

    for char in frist_rucksacks:
        for char_second in second_rucksacks:
            if char == char_second:
                if char != match_in_word:
                    match_in_word = char
    match.append(match_in_word)

for i in match:
    if i.isupper():
        value += ord(i) - 38
    else:
         value += ord(i) - 96
         
print(value)