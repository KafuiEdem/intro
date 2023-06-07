"""
    Create a Python script that reads a text file into a list and then converts the list into a string that has the entire file content.
    Use the test simpletext
"""

with open("sample_file.txt") as f:
    read_file = f.read().splitlines()
    my_string = '\n'.join(read_file)
    print(my_string)