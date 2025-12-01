import re
from itertools import combinations

with open('D11.txt') as file:
    space = file.read()

height, width, total_sum = space.count('\n') + 1, space.index('\n') + 1, 0
empty_rows = [row_num for row_num, row in enumerate(space.split()) if set(row) == {"."}]
empty_cols = [col_num for col_num in range(width - 1) if set(space[col_num::width]) == {"."}]
for g1, g2 in combinations(re.finditer('#', space), 2):
    g1, g2 = g1.start(), g2.start()
    x1, y1 = g1 % width, g1 // width
    x2, y2 = g2 % width, g2 // width
    total_sum += len([1 for row in empty_rows if min(y1, y2) < row < max(y1, y2)]) * (1000000 - 1)
    total_sum += len([1 for col in empty_cols if min(x1, x2) < col < max(x1, x2)]) * (1000000 - 1)
    total_sum += abs(x1 - x2) + y2 - y1
print(total_sum)