moves = ['L2', 'L5', 'L5', 'R5', 'L2', 'L4', 'R1', 'R1', 'L4', 'R2', 'R1', 'L1', 'L4', 'R1', 'L4', 'L4', 'R5', 'R3', 'R1', 'L1', 'R1', 'L5', 'L1', 'R5', 'L4', 'R2', 'L5', 'L3', 'L3', 'R3', 'L3', 'R4', 'R4', 'L2', 'L5', 'R1', 'R2', 'L2', 'L1', 'R3', 'R4', 'L193', 'R3', 'L5', 'R45', 'L1', 'R4', 'R79', 'L5', 'L5', 'R5', 'R1', 'L4', 'R3', 'R3', 'L4', 'R185', 'L5', 'L3', 'L1', 'R5', 'L2', 'R1', 'R3', 'R2', 'L3', 'L4', 'L2', 'R2', 'L3', 'L2', 'L2', 'L3', 'L5', 'R3', 'R4', 'L5', 'R1', 'R2', 'L2', 'R4', 'R3', 'L4', 'L3', 'L1', 'R3', 'R2', 'R1', 'R1', 'L3', 'R4', 'L5', 'R2', 'R1', 'R3', 'L3', 'L2', 'L2', 'R2', 'R1', 'R2', 'R3', 'L3', 'L3', 'R4', 'L4', 'R4', 'R4', 'R4', 'L3', 'L1', 'L2', 'R5', 'R2', 'R2', 'R2', 'L4', 'L3', 'L4', 'R4', 'L5', 'L4', 'R2', 'L4', 'L4', 'R4', 'R1', 'R5', 'L2', 'L4', 'L5', 'L3', 'L2', 'L4', 'L4', 'R3', 'L3', 'L4', 'R1', 'L2', 'R3', 'L2', 'R1', 'R2', 'R5', 'L4', 'L2', 'L1', 'L3', 'R2', 'R3', 'L2', 'L1', 'L5', 'L2', 'L1', 'R4']

axis = ['A']

locs = []

x = 0

y = 0

i = 0
while i <= len(moves) - 1:
    if moves[i][0] == 'L' and axis[i] == 'A':
        axis.append('D')
        for p in range(int(moves[i][1:])):
            x -= 1
            if [x, y] in locs:
                print('locale =', x, y, 'index =', i, 'dist =', abs(x) + abs(y))
                locs.append([x, y])
            else:
                locs.append([x, y])
        i += 1
    elif moves[i][0] == 'L' and axis[i] == 'B':
        axis.append('C')
        for p in range(int(moves[i][1:])):
            x += 1
            if [x, y] in locs:
                print('locale =', x, y, 'index =', i, 'dist =', abs(x) + abs(y))
                locs.append([x, y])
            else:
                locs.append([x, y])
        i += 1
    elif moves[i][0] == 'L' and axis[i] == 'C':
        axis.append('A')
        for p in range(int(moves[i][1:])):
            y += 1
            if [x, y] in locs:
                print('locale =', x, y, 'index =', i, 'dist =', abs(x) + abs(y))
                locs.append([x, y])
            else:
                locs.append([x, y])
        i += 1
    elif moves[i][0] == 'L' and axis[i] == 'D':
        axis.append('B')
        for p in range(int(moves[i][1:])):
            y -= 1
            if [x, y] in locs:
                print('locale =', x, y, 'index =', i, 'dist =', abs(x) + abs(y))
                locs.append([x, y])
            else:
                locs.append([x, y])
        i += 1
    elif moves[i][0] == 'R' and axis[i] == 'A':
        axis.append('C')
        for p in range(int(moves[i][1:])):
            x += 1
            if [x, y] in locs:
                print('locale =', x, y, 'index =', i, 'dist =', abs(x) + abs(y))
                locs.append([x, y])
            else:
                locs.append([x, y])
        i += 1
    elif moves[i][0] == 'R' and axis[i] == 'B':
        axis.append('D')
        for p in range(int(moves[i][1:])):
            x -= 1
            if [x, y] in locs:
                print('locale =', x, y, 'index =', i, 'dist =', abs(x) + abs(y))
                locs.append([x, y])
            else:
                locs.append([x, y])
        i += 1
    elif moves[i][0] == 'R' and axis[i] == 'C':
        axis.append('B')
        for p in range(int(moves[i][1:])):
            y -= 1
            if [x, y] in locs:
                print('locale =', x, y, 'index =', i, 'dist =', abs(x) + abs(y))
                locs.append([x, y])
            else:
                locs.append([x, y])
        i += 1
    elif moves[i][0] == 'R' and axis[i] == 'D':
        axis.append('A')
        for p in range(int(moves[i][1:])):
            y += 1
            if [x, y] in locs:
                print('locale =', x, y, 'index =', i, 'dist =', abs(x) + abs(y))
                locs.append([x, y])
            else:
                locs.append([x, y])
        i += 1
        
           
print(abs(x) + abs(y))




