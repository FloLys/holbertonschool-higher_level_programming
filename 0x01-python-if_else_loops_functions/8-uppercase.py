#!/usr/bin/python3
def uppercase(str):
    upstr = ''
    for i in str:
        lowchar = ord(i)
        if lowchar >= 97 and lowchar <= 122:
            upstr = upstr + chr((ord(i) - 32))
        else:
            upstr = upstr + chr((ord(i)))
    print(upstr)
