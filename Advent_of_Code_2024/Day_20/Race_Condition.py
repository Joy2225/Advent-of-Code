from collections import deque
def is_valid(x, y, map):
    return 0 <= x < len(map) and 0 <= y < len(map[0])

def bfs(map, start, end):
    queue = deque([start])
    i = 0

    while queue:
        x, y = queue[i]
        i += 1
        
        if x==end[0] and y==end[1]:
            return map[x][y]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny] == 0:
                map[nx][ny] = map[x][y] + 1
                queue.append((nx, ny))
    return None


data = [list(i) for i in open("D20.txt").read().splitlines()]
map = [[0]*len(data[0]) for _ in range(len(data))]

start = end = None
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "#":
            map[i][j] = -1
        elif data[i][j] == "S":
            start = (i,j)
        elif data[i][j] == "E":
            end = (i,j)

normal_time = bfs(map, start, end)

cheat_pos = []

for i in range(len(data)):
    for j in range(len(data[0])):
        if is_valid(i, j+1, data) and is_valid(i, j-1, data): 
            if (data[i][j] == "#" and data[i][j-1] == "." and data[i][j+1] == ".") or (data[i][j] == "#" and data[i][j-1] == "E" and data[i][j+1] == ".") or (data[i][j] == "#" and data[i][j-1] == "." and data[i][j+1] == "E"):
                cheat_pos.append((i,j))

        if is_valid(i+1, j, data) and is_valid(i-1, j, data):
            if (data[i][j] == "#" and data[i-1][j] == "." and data[i+1][j] == ".") or (data[i][j] == "#" and data[i-1][j] == "E" and data[i+1][j] == ".") or (data[i][j] == "#" and data[i-1][j] == "." and data[i+1][j] == "E"):
                cheat_pos.append((i,j))

count = {}
for i, j in cheat_pos:
    map = [[0 if cell != -1 else -1 for cell in row] for row in map]
    map[i][j] = 0
    time = bfs(map, start, end)
    map[i][j] = -1
    if normal_time-time:
        if normal_time-time in count:
            count[normal_time-time]+=1
        else:
            count[normal_time-time]=1

print(sum([j for i, j in count.items() if i >= 100]))
# 1293

# Above code is mine. BFS brute force. Takes a lot of time. Had to see how to do the optimied one. Credits:- Brian (Reddit)
DIRS = NORTH,EAST,SOUTH,WEST = [(0,-1), (1,0), (0,1), (-1,0)]

def taxicab(dist: int):
    """All points within taxicab distance of (0,0)"""
    for y in range(-dist, dist+1):
        for x in range(-(dist-abs(y)), dist-abs(y)+1):
            yield x,y

def read_input(path="D20.txt"):
    points = set()
    start_pos = end_pos = None
    with open(path) as f:
        for y,line in enumerate(f):
            line = line.strip()
            if not line: 
                break
            for x,ch in enumerate(line):
                if ch in 'SE.':
                    points.add((x,y))
                    if ch == 'S':
                        start_pos = x,y
                    elif ch == 'E':
                        end_pos = x,y
    assert start_pos is not None
    assert end_pos is not None
    return points, start_pos, end_pos

def get_track(points, start_pos, end_pos):
    x,y = start_pos
    track = {} # pos: score
    score = 0
    while (x,y) != end_pos:
        track[x,y] = score
        for dx,dy in DIRS:
            newpos = x+dx, y+dy
            if newpos not in track and newpos in points:
                x,y = newpos
                break
        else:
            raise Exception("No route to end")
        score += 1
    track[x,y] = score # End
    return track

def num_cheats(track, dist, saving_required):
    tot=0
    for (x,y), score in track.items():
        for dx,dy in taxicab(dist):
            if dy==dx==0: continue
            x2, y2 = x+dx, y+dy

            if (x2,y2) in track:
                saved = track[x2,y2] - score - abs(dx) - abs(dy)
                if saved >= saving_required:
                    tot += 1

    return tot

points, start_pos, end_pos = read_input()
track = get_track(points, start_pos, end_pos)
print(num_cheats(track, 2, 100))
print(num_cheats(track, 20, 100))


    
