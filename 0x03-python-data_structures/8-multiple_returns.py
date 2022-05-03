#!/usr/bin/python3
def multiple_returns(sentence):
    char = ""
    if sentence:
        char = sentence[0]
    if not sentence:
        char = None
    length_char = (len(sentence), char)
    return length_char
