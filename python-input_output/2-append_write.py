#!/usr/bin/python3


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text
    file and returns the number of characters added."""
    with open(filename, 'a', encoding="utf-8") as f:
        nb_chars = f.write(text)
    return nb_chars
