moves = ['R8', 'R4', 'R4', 'R8']

axis = ['A']

locs = []

x = 0

y = 0

i = 0
while i <= len(moves) - 1:
    if moves[i][0] == 'L' and axis[i] == 'A':
        axis.append('D')
        x -= int(moves[i][1:])
        i += 1
        if [x, y] in locs:
            print(x, y, i)
        locs.append([x, y])
    elif moves[i][0] == 'L' and axis[i] == 'B':
        axis.append('C')
        x += int(moves[i][1:])
        i += 1
        if [x, y] in locs:
            print(x, y, i)
        locs.append([x, y])
    elif moves[i][0] == 'L' and axis[i] == 'C':
        axis.append('A')
        y += int(moves[i][1:])
        i += 1
        if [x, y] in locs:
            print(x, y, i)
        locs.append([x, y])
    elif moves[i][0] == 'L' and axis[i] == 'D':
        axis.append('B')
        y -= int(moves[i][1:])
        i += 1
        if [x, y] in locs:
            print(x, y, i)
        locs.append([x, y])
    elif moves[i][0] == 'R' and axis[i] == 'A':
        axis.append('C')
        x += int(moves[i][1:])
        i += 1
        if [x, y] in locs:
            print(x, y, i)
        locs.append([x, y])
    elif moves[i][0] == 'R' and axis[i] == 'B':
        axis.append('D')
        x -= int(moves[i][1:])
        i += 1
        if [x, y] in locs:
            print(x, y, i)
        locs.append([x, y])
    elif moves[i][0] == 'R' and axis[i] == 'C':
        axis.append('B')
        y -= int(moves[i][1:])
        i += 1
        if [x, y] in locs:
            print(x, y, i)
        locs.append([x, y])
    elif moves[i][0] == 'R' and axis[i] == 'D':
        axis.append('A')
        y += int(moves[i][1:])
        i += 1
        if [x, y] in locs:
            print(x, y, i)
        locs.append([x, y])
        
           
print(abs(x) + abs(y))

print(locs)