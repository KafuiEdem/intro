import csv 

with open("passwd.csv") as f:
    reader = csv.reader(f,delimiter=":",lineterminator="\n")

    for row in reader:
        print(row)