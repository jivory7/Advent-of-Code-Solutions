stacks = [[['N'], ['Z']], [['D'], ['C'], ['M']], [['P']]]

moves = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]

#w = 2

#x = moves[w][0] #number of crates moved

#y = moves[w][1] #starting stack
    
#z = moves[w][2] #ending stack

#print(x)

#for m in range(x):
    #stacks[z-1].insert(0, stacks[y-1][(x-1)])
    #stacks[y-1].remove(stacks[y-1][(x-1)])
    #x -= 1
     
#print(stacks)

w = 0

while w <= len(moves) - 1:
    x = moves[w][0] #number of crates moved
    y = moves[w][1] #starting stack
    z = moves[w][2] #ending stack
    c = x
    for m in range(x):
        stacks[z-1].insert(0, stacks[y-1].pop(x-1))
        x -= 1
    w += 1
    
b = 0

while b <= len(stacks) - 1:
    print(stacks[b][0])
    b += 1


    

