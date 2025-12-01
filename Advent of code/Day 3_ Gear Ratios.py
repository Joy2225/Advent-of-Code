import re

with open('D3.txt') as file:
    input_data = file.read().split()

# Part 1
grid = ['.' * (len(input_data[0]) + 2)] * 2
grid[1:1] = map(".{}.".format, input_data)
total_sum = 0

for index, row in enumerate(grid[1:-1], 1):# grid[1:-1], 1 -> this 1 is specifying what the starting index should be
    for number in re.finditer(r'\d+', row):
        start, stop = number.span()
        for section in grid[index - 1:index + 2]:
            if re.sub(r'[\d\.]', '', section[start - 1:stop + 1]):
                total_sum += int(number.group())
                break

print(total_sum)

# Part 2
from collections import defaultdict
from math import prod


grid = ['.' * (len(input_data[0]) + 2)] * 2
grid[1:1] = map(".{}.".format, input_data)
total_sum = 0

gear_list = defaultdict(list)

for index, row in enumerate(grid[1:-1], 1):
    for number in re.finditer(r'\d+', row):
        start, stop = number.span()
        for row_offset, section in enumerate(grid[index - 1:index + 2]):
            for col_offset, char in enumerate(section[start - 1:stop + 1]):
                if char not in '0123456789.':
                    gear_list[(index + row_offset - 1, start + col_offset - 1)].append(int(number.group()))

for parts in gear_list.values():
    if len(parts) == 2:
        total_sum += prod(parts)

print(total_sum)