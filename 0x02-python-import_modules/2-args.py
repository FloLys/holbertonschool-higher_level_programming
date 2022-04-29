#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv[1:])    
    # 0 args
    if argc == 0:
        print("0 arguments.")
    # 1 argument
    elif argc == 1:
        print(f"1 argument:\n1: {argv[1]}")
    # many arguments
    else:
        print(f"{argc - 1} arguments:")
        for i in range(1, argc):
            print(f"{i}: {argv[i]}")
