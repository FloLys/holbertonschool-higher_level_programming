#!/usr/bin/python3
flag = False
for letter in range(25, -1, -1):
    if flag:
        letter = letter + 65
        flag = False
    else:
        letter = letter + 97
        flag = True
    print(chr(letter), end='')
