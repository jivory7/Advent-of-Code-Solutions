ds = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

#print(ds[3:7])

#print(set(ds[3:7]))

x = 0

for m in ds:
    if len(set(ds[x:x+14])) < 14:
        x += 1
    elif len(set(ds[x:x+14])) == 14:
        print(ds[x:x+14])
        print(ds.find(ds[x:x+14]) + 14)
        break