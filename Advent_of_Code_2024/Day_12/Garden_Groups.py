from collections import deque, defaultdict

def parse_map(garden_map):
    rows = len(garden_map)
    cols = len(garden_map[0])

    def find_area(start_row, start_col):
        queue = deque([(start_row, start_col)])
        visited.add((start_row, start_col))
        plant_type = garden_map[start_row][start_col]

        area = 0
        perimeter = 0

        while queue:
            r, c = queue.popleft()
            area += 1

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    perimeter += 1
                elif garden_map[nr][nc] != plant_type:
                    perimeter += 1
                elif (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return area, perimeter

    visited = set()
    prices = []

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                area, perimeter = find_area(row, col)
                price = area * perimeter
                prices.append(price)

    return prices

# Example usage
garden_map = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE"
]

total_price = sum(parse_map(garden_map))
print(f"Total price of fencing all regions: {total_price}")