# Python - Input/Output

- **[0. Read file](./0-read_file.py)**

- Write a function that reads a text file (UTF8) and prints it to stdout:
  - Prototype: def read_file(filename=""):
  - You must use the with statement
  - You don't need to manage file permission or file doesn't exist exceptions.
  - You are not allowed to import any module

- **[1. Write to a file](./1-write_file.py)**

- Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
  - Prototype: def write_file(filename="", text=""):
  - You must use the with statement
  - You don't need to manage file permission exceptions.
  - Your function should create the file if doesn't exist.
  - Your function should overwrite the content of the file if it already exists.
  - You are not allowed to import any module

- **[2. Append to a file](./2-append_write.py)** 

- Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
  - Prototype: def append_write(filename="", text=""):
  - If the file doesn't exist, it should be created
  - You must use the with statement
  - You don't need to manage file permission or file doesn't exist exceptions.
  - You are not allowed to import any module

- **[3. To JSON string](./3-to_json_string.py)**

- Write a function that returns the JSON representation of an object (string):
  - Prototype: def to_json_string(my_obj):
  - You don't need to manage exceptions if the object can't be serialized.

- **[4. From JSON string to Object](./4-from_json_string.py)**

- Write a function that returns an object (Python data structure) represented by a JSON string:
  - Prototype: def from_json_string(my_str):
  - You don't need to manage exceptions if the JSON string doesn't represent an object.

- **[5. Save Object to a file](./5-save_to_json_file.py)**

- Write a function that writes an Object to a text file, using a JSON representation:
  - Prototype: def save_to_json_file(my_obj, filename):
  - You must use the with statement
  - You don't need to manage exceptions if the object can't be serialized.
  - You don't need to manage file permission exceptions.
   
- **[6. Print sorted dictionary](./6-print_sorted_dictionary.py)**

- Write a function that prints a dictionary by ordered keys.
  - Prototype: def print_sorted_dictionary(a_dictionary):
  - You can assume that all keys are strings
  - Keys should be sorted by alphabetic order
  - Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
  - Dictionary values can have any type
  - You are not allowed to import any module
   
- **[7. Update dictionary](./7-update_dictionary.py)**

- Write a function that replaces or adds key/value in a dictionary.
  - Prototype: def update_dictionary(a_dictionary, key, value):
  - key argument will be always a string
  - value argument will be any type
  - If a key exists in the dictionary, the value will be replaced
  - If a key doesn’t exist in the dictionary, it will be created
  - You are not allowed to import any module

- **[8. Simple delete by key](./8-simple_delete.py)**

- Write a function that deletes a key in a dictionary.
  - Prototype: def simple_delete(a_dictionary, key=""):
  - key argument will be always a string
  - If a key doesn’t exist, the dictionary won’t change
  - You are not allowed to import any module

  - **[9. Multiply by 2](./9-multiply_by_2.py)**

- Write a function that returns a new dictionary with all values multiplied by 2
  - Prototype: def multiply_by_2(a_dictionary):
  - You can assume that all values are only integers
  - Returns a new dictionary
  - You are not allowed to import any module

  - **[10. Best score](./10-best_score.py)**

- Write a function that returns a key with the biggest integer value.
  - Prototype: def best_score(a_dictionary):
  - You can assume that all values are only integers
  - If no score found, return None
  - You can assume all students have a different score
  - You are not allowed to import any module

  - **[11. Multiply by using map](./11-multiply_list_map.py)**

- Write a function that returns a list with all values multiplied by a number without using any loops.
  - Prototype: def multiply_list_map(my_list=[], number=0):
  - Returns a new list:
    - Same length as my_list
    - Each value should be multiplied by number
  - Initial list should not be modified
  - You are not allowed to import any module
  - You have to use map
  - Your file should be max 3 lines

  - **[12. Roman to Integer](./12-roman_to_int.py)**

- Technical interview preparation:
  - You are not allowed to google anything
  - Whiteboard first
- Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.
  - You can assume the number will be between 1 to 3999.
  - def roman_to_int(roman_string) must return an integer
  - If the roman_string is not a string or None, return 0