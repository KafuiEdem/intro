with open("device.txt") as f:
    read_file = f.read().splitlines()

    new_device = []
    for i in read_file:
        new_device.append(i.split(":"))
    print(new_device)