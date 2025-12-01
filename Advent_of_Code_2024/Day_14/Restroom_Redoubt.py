import re

# Part 1
data = open("D14.txt").read().splitlines()
pos = []
vel = []

for line in data:
    pos.append(re.findall(r"p=([0-9]+),([0-9]+)", line)[0])
    vel.append(re.findall(r"v=(-?[0-9]+),(-?[0-9]+)", line)[0])

q_1, q_2, q_3, q_4 = 0, 0, 0, 0

for i, j in zip(pos, vel):
    x = int(i[0])
    y = int(i[1])
    dx = int(j[0])
    dy = int(j[1])

    nx = (100*dx + x) % 101
    ny = (100*dy + y) % 103

    if nx < 50 and ny < 51:
        q_1 += 1
    elif nx < 50 and ny > 51:
        q_2 += 1
    elif nx > 50 and ny < 51:
        q_3 += 1
    elif nx > 50 and ny > 51:
        q_4 += 1

print(q_1*q_2*q_3*q_4)
# 224438715

# Track position of each robot each second and write the map to a file
seconds = 100  # Number of seconds to track
map_file = open("robot_map.txt", "w")

# Initialize positions
positions = [(int(p[0]), int(p[1])) for p in pos]
velocities = [(int(v[0]), int(v[1])) for v in vel]

t = 0

while True:
    # Create a map for the current second
    current_map = [["." for _ in range(102)] for _ in range(104)]
    
    for idx, (x, y) in enumerate(positions):
        dx, dy = velocities[idx]
        x = (x + dx) % 101
        y = (y + dy) % 103
        
        positions[idx] = (x, y)
        current_map[y][x] = "#"
    
    # Write the current map to the file
    map_file.write(f"Second {t+1}:\n")
    for row in current_map:
        map_file.write("".join(row) + "\n")
    map_file.write("\n")
    t+=1

# 7603 seconds
# Kindoff bruteforced this