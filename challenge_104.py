""" 
    Create a Python function called tail that reads the last n lines of a text file.
    The function has two arguments: the file name and n (the number of lines to read). This is similar to the Linux `tail` command.
    Example: tail('sample_file.txt', 5) will return the last 5 lines from sample_file.txt.
"""
import time

def tail(file_name:str, n:int):
    with open(file_name,"r") as file:
        read = file.readlines()
        last_line = read[len(read)-n]
        return last_line

while True:
    t = tail("sample_file.txt",8)
    print(t)
    time.sleep(3)
    print("")