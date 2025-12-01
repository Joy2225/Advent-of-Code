from sys import argv
from heapq import heappop, heappush
from math import inf

with open(argv[1]) as f:
    lines = [list(l.strip()) for l in f]

dimy, dimx = len(lines), len(lines[0])
start = end = None
for y in range(dimy):
    for x in range(dimx):
        if lines[y][x] == 'S':
            start = (x, y)
        elif lines[y][x] == 'E':
            end = (x, y)

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Up, Right, Down, Left

visited = dict()
q = list()
lowscore = inf
paths = list()

heappush(q, (0, start, 1, ""))  # Initial state: score=0, start position, facing right, no path
while q:
    score, (x, y), d, path = heappop(q)
    if score > lowscore:
        break
    if ((x, y), d) in visited and visited[((x, y), d)] < score:
        continue
    visited[((x, y), d)] = score
    if (x, y) == end:
        lowscore = score
        paths.append(path)
    
    # Move forward
    nx, ny = x + dirs[d][0], y + dirs[d][1]
    if 0 <= nx < dimx and 0 <= ny < dimy and lines[ny][nx] != '#':
        heappush(q, (score + 1, (nx, ny), d, path + "F"))
    
    # Turn right
    heappush(q, (score + 1000, (x, y), (d + 1) % 4, path + "R"))
    
    # Turn left
    heappush(q, (score + 1000, (x, y), (d - 1) % 4, path + "L"))

tiles = set()
tiles.add(start)
for p in paths:
    t = start
    d = 1  # Start facing right
    for c in p:
        if c == "L":
            d = (d - 1) % 4
        elif c == "R":
            d = (d + 1) % 4
        elif c == "F":
            t = (t[0] + dirs[d][0], t[1] + dirs[d][1])
            tiles.add(t)

print(f"Shortest path: {lowscore}")
print(f"Optimal viewing positions: {len(tiles)}")