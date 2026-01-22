#!/usr/bin/python3
"""Prints a text with 2 new lines after each of these characters: ., ? and:
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each . ? :

    Args:
        text (str): The input text

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        c = text[i]
        if c in '.?:':
            print(c, end="")
            print()
            print()
            i += 1
            while i < len(text) and text[i].isspace():
                i += 1
        else:
            print(c, end="")
            i += 1
