new_device = []
with open("devices.txt") as f:
    read_file = f.readlines()[1:]

for file in read_file:
    new_device.append(file.split(":"))
print(new_device)

for i in new_device:
    print(i[1])