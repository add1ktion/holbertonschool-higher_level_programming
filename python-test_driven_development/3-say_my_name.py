#!/usr/bin/python3
"""
Prints My name is <first name> <last_name>.

Prototype: def say_my_name(first_name, last_name=""):
first_name and last_name must be strings, otherwise raise TypeError.
Usage: say_my_name("John", "Smith") or say_my_name("Bob").
"""
def say_my_name(first_name, last_name=""):
    """Prints formatted name with validation.
    
    Args:
        first_name (str): First name
        last_name (str): Last name (default "")
    
    Raises:
        TypeError: If first_name or last_name not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
    