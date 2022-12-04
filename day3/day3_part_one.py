input = open("day3.txt","r")
lst = str(input.read())
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

for check in match:
    if check == 'a':
        value += 1
    if check == 'b':
        value += 2
    if check == 'c':
        value += 3
    if check == 'd':
        value += 4
    if check == 'e':
        value += 5
    if check == 'f':
        value += 6
    if check == 'g':
        value += 7
    if check == 'h':
        value += 8
    if check == 'i':
        value += 9
    if check == 'j':
        value += 10
    if check == 'k':
        value += 11
    if check == 'l':
        value += 12
    if check == 'm':
        value += 13
    if check == 'n':
        value += 14
    if check == 'o':
        value += 15
    if check == 'p':
        value += 16
    if check == 'q':
        value += 17
    if check == 'r':
        value += 18
    if check == 's':
        value += 19
    if check == 't':
        value += 20
    if check == 'u':
        value += 21
    if check == 'v':
        value += 22
    if check == 'w':
        value += 23
    if check == 'x':
        value += 24
    if check == 'y':
        value += 25
    if check == 'z':
        value += 26
    if check == 'A':
        value += 27
    if check == 'B':
        value += 28
    if check == 'C':
        value += 29
    if check == 'D':
        value += 30
    if check == 'E':
        value += 31
    if check == 'F':
        value += 32
    if check == 'G':
        value += 33
    if check == 'H':
        value += 34
    if check == 'I':
        value += 35
    if check == 'J':
        value += 36
    if check == 'K':
        value += 37
    if check == 'L':
        value += 38
    if check == 'M':
        value += 39
    if check == 'N':
        value += 40
    if check == 'O':
        value += 41
    if check == 'P':
        value += 42
    if check == 'Q':
        value += 43
    if check == 'R':
        value += 44
    if check == 'S':
        value += 45
    if check == 'T':
        value += 46
    if check == 'U':
        value += 47
    if check == 'V':
        value += 48
    if check == 'W':
        value += 49
    if check == 'X':
        value += 50
    if check == 'Y':
        value += 51
    if check == 'Z':
        value += 52
print(value)