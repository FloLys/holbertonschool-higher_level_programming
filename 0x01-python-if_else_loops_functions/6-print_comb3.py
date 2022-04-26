#!/usr/bin/python3
flag = False
for i in range(10):
    for j in range(i+1, 10):
        if flag:
            print(", ", end='')
        else:
            flag = True
        print("{}{}".format(i, j), end='')
print()
