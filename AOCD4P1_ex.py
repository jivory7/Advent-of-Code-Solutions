ids = [[[2, 4], [6, 8]], [[2, 3], [4, 5]], [[5, 7], [7, 9]], [[2, 8], [3, 7]], [[6, 6], [4, 6]], [[2, 6], [4, 8]]]

x = 0
y = 0

def rangeset(r1, r2):
    return set(range(r1, r2+1))

for m in ids:
    if rangeset(ids[x][0][0], ids[x][0][1]).intersection(rangeset(ids[x][1][0], ids[x][1][1])) != set():
        y += 1
    x += 1

print(y)

q = {2, 3}
p = {4, 5}

print(q.intersection(p))