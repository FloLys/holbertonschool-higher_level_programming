#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        print(number, end='')
        return number
    elif number > 0:
        lastdigit = number % 10
        print(lastdigit, end='')
        return lastdigit
    else:
        lastdigit = (-number % 10)
        print(lastdigit, end='')
        return lastdigit
