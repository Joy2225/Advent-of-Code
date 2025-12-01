import heapq

def parse_maze(maze_str):
    maze = maze_str.strip().split("\n")
    start = end = None
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == 'S':
                start = (x, y)
            elif char == 'E':
                end = (x, y)
    return maze, start, end

def is_within_bounds(maze, x, y):
    return 0 <= y < len(maze) and 0 <= x < len(maze[0]) and maze[y][x] != '#'

def dijkstra(maze, start, end):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, South, West, North
    direction_cost = 1000
    move_cost = 1

    pq = [(0, start[0], start[1], 0)]  # (cost, x, y, direction_index)
    visited = set()

    while pq:
        cost, x, y, current_dir = heapq.heappop(pq)

        if (x, y, current_dir) in visited:
            continue
        visited.add((x, y, current_dir))

        if (x, y) == end:
            return cost

        for new_dir, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            if not is_within_bounds(maze, nx, ny):
                continue

            new_cost = cost + move_cost
            if new_dir != current_dir:
                new_cost += direction_cost

            heapq.heappush(pq, (new_cost, nx, ny, new_dir))

    return float('inf')  # If no path is found

def solve_reindeer_maze(maze_str):
    maze, start, end = parse_maze(maze_str)
    return dijkstra(maze, start, end)

maze_input = open("D16.txt").read()

print(solve_reindeer_maze(maze_input))




