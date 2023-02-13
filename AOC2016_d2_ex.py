buttons = [['U', 'L', 'L'], ['R', 'R', 'D', 'D', 'D'], ['L', 'U', 'R', 'D', 'L'], ['U', 'U', 'U', 'U', 'D']]

numpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

numpad2 = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 'A', 'B', 'C', 0], [0, 0, 'D', 0, 0]]

def passgen(x):
    v = 2
    z = 0
    for m in x:
        for n in m:
            if n == 'U' and v > 0 and numpad2[v-1][z] != 0:
                v -= 1
            if n == 'D' and v < 4 and numpad2[v+1][z] != 0:
                v += 1
            if n == 'L' and z > 0 and numpad2[v][z-1] != 0:
                z -= 1
            if n == 'R' and z < 4 and numpad2[v][z+1] != 0:
                z += 1
            
        print(numpad2[v][z])

passgen(buttons)