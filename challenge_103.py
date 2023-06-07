"""
    Create a Python script that removes all empty lines including those that contain only spaces from a file.
"""

with open("file.txt") as f:
    read = f.read().split()
    with open("file2.txt","w") as a:
        for i in read:
            a.write(i.strip())
            print(i.strip())