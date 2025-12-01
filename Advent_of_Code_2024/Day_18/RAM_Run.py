def bfs(map):
    queue = [(0,0)]

    i = 0

    while i < len(queue):
        y, x = queue[i]
        i += 1
        
        if x==70 and y==70:
            return map[x][y]

        if x-1 >= 0:
            if map[x-1][y] == 0:
                map[x-1][y] = map[x][y] + 1
                queue.append((y, x-1))
        if x+1 < 71:
            if map[x+1][y] == 0:
                map[x+1][y] = map[x][y] + 1
                queue.append((y, x+1))
        if y-1 >= 0:
            if map[x][y-1] == 0:
                map[x][y-1] = map[x][y] + 1
                queue.append((y-1, x))
        if y+1 < 71:
            if map[x][y+1] == 0:
                map[x][y+1] = map[x][y] + 1
                queue.append((y+1, x))
    return None


data = open("D18.txt").read().splitlines()[:1024]
map = [[0]*71 for _ in range(71)]


for i in data:
    x, y = int(i.split(",")[0]), int(i.split(",")[1])
    map[y][x] = -1



print(bfs(map)) 


data = open("D18.txt").read().splitlines()
for val in range(1025, len(data)):
    map = [[0]*71 for _ in range(71)]

    for i in data[:val]:
        x, y = int(i.split(",")[0]), int(i.split(",")[1])
        map[y][x] = -1
    if bfs(map) == None:
        print(x,y)
        break
    
    

    

