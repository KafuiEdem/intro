import csv

with open("airtravel.csv",'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)#if you don't want to read the header
    year_1958 = dict()
    for file in csv_reader:
        year_1958[file[0]] = file[1]

    print(year_1958)
    max_1958 = max(year_1958.values())
    print(max_1958)
    for item,value in year_1958.items():
        if value == max_1958:
            print(f"Busiest month in 1958 is {item} ")