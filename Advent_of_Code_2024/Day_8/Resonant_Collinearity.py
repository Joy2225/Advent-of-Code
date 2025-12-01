def check_coord(row_no, col_no, coord):
    return 0 <= coord[0] < row_no and 0 <= coord[1] < col_no

# Part 1 and 2
data = open("D8.txt", "r").read().splitlines()
data = [list(i) for i in data]
row_no = len(data)
col_no = len(data[0])

ele_set = {char for row in data for char in row if char != '.'}

unique = set()

ele_pos = {char: [] for char in ele_set}
for i in range(row_no):
    for j in range(col_no):
        if data[i][j] != '.':
            ele_pos[data[i][j]].append((i, j))
            unique.add((i, j))




for key, positions in ele_pos.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            pos1 = positions[i]
            pos2 = positions[j]

            dx = pos2[0] - pos1[0]
            dy = pos2[1] - pos1[1]
            
            # antinode1 = [(pos1[0] + dx, pos1[1] - dy)] # Uncomment for part 1
            # antinode2 = [(pos2[0] + dx, pos2[1] + dy)] # Uncomment for part 1

            c = 1                                                                    # Uncomment for part 2
            while check_coord(row_no, col_no, (pos1[0] - c * dx, pos1[1] - c * dy)): # Uncomment for part 2
                unique.add((pos1[0] - c * dx, pos1[1] - c * dy))                     # Uncomment for part 2
                c += 1                                                               # Uncomment for part 2
            
            c = 1                                                                    # Uncomment for part 2
            while check_coord(row_no, col_no, (pos2[0] + c * dx, pos2[1] + c * dy)): # Uncomment for part 2
                unique.add((pos2[0] + c * dx, pos2[1] + c * dy))                     # Uncomment for part 2
                c += 1                                                               # Uncomment for part 2

            # for antinode1 in antinode1:                    # Uncomment for part 1
            #     if check_coord(row_no, col_no, antinode1): # Uncomment for part 1
            #         unique.add(antinode1)                  # Uncomment for part 1
            # for antinode2 in antinode2:                    # Uncomment for part 1
            #     if check_coord(row_no, col_no, antinode2): # Uncomment for part 1
            #         unique.add(antinode2)                  # Uncomment for part 1


print(len(unique))
# Part 1 :- 291
# Part 2 :- 1015