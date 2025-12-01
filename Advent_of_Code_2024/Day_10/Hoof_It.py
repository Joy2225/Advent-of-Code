def valid(x, y):
    return 0 <= x < len(data) and 0 <= y < len(data[0])

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
total = 0  

def reachable_1(x, y, data, stack):
    if data[x][y] == '9':
        stack.add((x, y))  
        return
    
    for i, j in direction:
        if valid(x + i, y + j) and data[x + i][y + j] == str(int(data[x][y]) + 1):
            reachable_1(x + i, y + j, data, stack)
    return stack  

data = [list(i) for i in open("D10.txt", "r").read().split("\n")]
zero_idx = [(i, j) for i in range(len(data)) for j in range(len(data[i])) if data[i][j] == "0"]

for i, j in zero_idx:
    stack = set()
    total += len(reachable_1(i, j, data, stack))

print(total)
# 550

total = 0 

def reachable_2(x, y, data):
    global total
    if data[x][y] == '9':
        total+=1  
        return
    
    for i, j in direction:
        if valid(x + i, y + j) and data[x + i][y + j] == str(int(data[x][y]) + 1):
            reachable_2(x + i, y + j, data)
    
data = [list(i) for i in open("D10.txt", "r").read().split("\n")]
zero_idx = [(i, j) for i in range(len(data)) for j in range(len(data[i])) if data[i][j] == "0"]

for i, j in zero_idx:
    stack = set()
    reachable_2(i, j, data)

print(total)
# 1255