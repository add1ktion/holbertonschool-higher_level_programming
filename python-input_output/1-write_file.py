#!/usr/bin/python3


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file and
    returns the number of characters written."""
    with open(filename, 'w', encoding="utf-8") as f:
        nb_chars = f.write(text)
    return nb_chars
