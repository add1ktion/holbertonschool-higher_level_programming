#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = False
    for c in text:
        if c in '.?:':
            print(c, end="")
            print()
            skip_space = True
            continue
        if skip_space and c == ' ':
            skip_space = False
            print()
        else:
            print(c, end="")