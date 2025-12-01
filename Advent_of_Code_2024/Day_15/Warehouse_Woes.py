data = open("D15.txt").read().split("\n\n")
moves = ''.join(data[1].split("\n"))
map = [list(i) for i in data[0].split("\n")]
row, col = 0, 0

def is_O(map, i, j, x, y):
    # print(i, j, x, y)
    dx = x
    dy = y
    while map[i+x][j+y] == "O":
        
        x += dx
        y += dy
        # print(i, j, x, y)
    
    if map[i+x][j+y] == ".":
        map[i+x][j+y] = "O"
        return 0
    else:
        return -1

def simulate(map, i, j, x, y):
    char = map[i+x][j+y]
    if char == "#":
        return -1
    elif char == ".":
        map[i+x][j+y] = "@"
        map[i][j] = "."
        return 0
    else:
        if not (-1 == is_O(map, i, j, x, y)):
            map[i+x][j+y] = "@"
            map[i][j] = "."
        else:
            return -1

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '@':
            row, col = i, j
            break

for move in moves:
    if move == "^":
        if not (-1 == simulate(map, row, col, -1, 0)):
            row -= 1
    elif move == "v":
        if not (-1 == simulate(map, row, col, 1, 0)):
            row += 1
    elif move == ">":
        if not (-1 == simulate(map, row, col, 0, 1)):
            col += 1
    elif move == "<":
        if not (-1 == simulate(map, row, col, 0, -1)):
            col -= 1

total_sum = 0

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "O":
            total_sum += i*100+j

print(total_sum)
# 1426855

def extract_component(map, r, c, dr, dc):
  if map[r][c] in ['#', '.']: return []
  ch = map[r][c]
  map[r][c] = '.'
  component = [(r, c, ch)]
  component.extend(extract_component(map, r + dr, c + dc, dr, dc))
  if ch == '[':
    component.extend(extract_component(map, r, c + 1, dr, dc))
  if ch == ']':
    component.extend(extract_component(map, r, c - 1, dr, dc))
  return component

def solve(map, moves):
  robot_r, robot_c = next((r, row.index('@'))
                          for r, row in enumerate(map)
                          if '@' in row)
  for move in moves:
    if move == 'v': dr, dc = 1, 0
    elif move == '^': dr, dc = -1, 0
    elif move == '>': dr, dc = 0, 1
    elif move == '<': dr, dc = 0, -1
    else: continue

    component = extract_component(map, robot_r, robot_c, dr, dc)
    if all(map[r + dr][c + dc] == '.' for r, c, _ in component):
      component = [(r + dr, c + dc, ch) for r, c, ch in component]
      robot_r, robot_c = robot_r + dr, robot_c + dc
    for rr, cc, ch in component:
      map[rr][cc] = ch
 
  return sum(sum(r * 100 + c for c, ch in enumerate(row) if ch in ['O', '[']) for r, row in enumerate(map))

map, moves = open("D15.txt").read().split('\n\n')
map1 = [list(row) for row in map.split('\n')]
print(solve(map1, moves))

def double(ch):
  if ch == '@': return ['@', '.']
  elif ch == '.': return ['.', '.']
  elif ch == '#': return ['#', '#']
  elif ch == 'O': return ['[', ']']
  else: raise Exception("Unexpected char " + ch)

map2 = [sum((double(ch) for ch in row), []) for row in map.split('\n')]
print(solve(map2, moves))