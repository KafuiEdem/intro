"""
    Consider this text file that contains multiple duplicate MAC addresses.
    Create a new file that contains only unique MAC addresses. Each MAC should be on its own line.
"""

with open("macs.txt") as mac:
    read_mac = mac.read().splitlines()
    with open("new_macs.txt","w") as f:
        for i in read_mac:
            s = list(dict.fromkeys(i.split(" ")))
            for u in s:
                write = f.write(f'{u}\n')