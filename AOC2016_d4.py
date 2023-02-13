with open(r"C:\Users\Justin\Desktop\AOC2022\AOC2016_Day4_input.txt") as f:
    data = f.read().splitlines()

for i in range(len(data)):
    data[i] = data[i].split('-')

for m in data:
    m[-1] = m[-1].strip(']').split('[')

data1 = []

for m in data:
    m = [''.join(m[0:-1]), m[-1]]
    data1.append(m)

freqs = []

#sorts characters by frequency. tie is broken by alphabetical order.
for i in range(len(data1)):
    freq = []
    for m in set(data1[i][0]):
        x = data1[i][0].count(m)
        freq.append((x, m))
    freq.sort(key = lambda x: x[1])
    freq.sort(key = lambda x: x[0], reverse=True)
    freqs.append(freq)

keys = []

for i in range(len(freqs)):
    key = []
    for m in freqs[i][0:5]:
        key.append(m[1])
    keys.append(key)

keys1 = []

for m in keys:
    m = [''.join(m[0:])]
    keys1.append(m)

x = 0

rooms = []

for i in range(len(data1)):
    if keys1[i][0] == data1[i][1][1]:
        rooms.append(data1[i])
        x += int(data1[i][1][0])

print(x)

print(rooms[0][0])
print(int(rooms[0][1][0]))

 

    

print(rooms[0][0])

