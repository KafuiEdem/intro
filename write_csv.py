import csv

with open("people.csv","a") as f:
    csv_write = csv.writer(f)
    csv_data = (5,"Ann","Amsterdem")
    csv_write.writerow(csv_data)

with open("numbers.csv","w",newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["x","x**2","x**3","x**4"])
    for i in range(1,101):
        writer.writerow([i,i**2,i**3,i**4])