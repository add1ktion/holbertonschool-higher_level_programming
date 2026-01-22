#!/usr/bin/python3
"""
Text indentation module
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text to process

    Raises:
        TypeError: If text is not a string
    """
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
