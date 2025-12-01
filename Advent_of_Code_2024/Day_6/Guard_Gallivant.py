import copy
def isSafe(i, j, data):
     
    if data[i][j] != "#":
        return True
    return False



data = open('D6.txt', "r").read()
temp_data = data.replace("\n", "")
tot_idx = temp_data.index("^")
data = [list(i) for i in data.split("\n")]
guard_row = tot_idx//len(data[0])
guard_col = tot_idx%len(data[0])
# print(guard_row, guard_col)
curr_guard_row = guard_row -1
curr_guard_col = guard_col
total = 0
dist = 0


while True:

    if curr_guard_row < 0 or curr_guard_col < 0 or curr_guard_row >= len(data) or curr_guard_col >= len(data[0]):
        if data[guard_row][guard_col] != "X":
            total+=1
        dist+=1
        break

    if curr_guard_col == guard_col and curr_guard_row == guard_row-1:
        if isSafe(curr_guard_row, curr_guard_col, data):              
            dist+=1
            if data[guard_row][guard_col] != "X":                
                total += 1
                data[guard_row][guard_col] = "X"
            guard_row -= 1
            curr_guard_row -=1
            continue
            
        else:
            curr_guard_row = guard_row
            curr_guard_col = guard_col+1
            continue

    elif curr_guard_col == guard_col and curr_guard_row == guard_row+1:
        if isSafe(curr_guard_row, curr_guard_col, data):
            dist+=1
            if data[guard_row][guard_col] != "X":                
                total += 1
                data[guard_row][guard_col] = "X"
            guard_row += 1
            curr_guard_row +=1
            continue
        else:
            curr_guard_row = guard_row
            curr_guard_col = guard_col-1
            continue
    elif curr_guard_col == guard_col-1 and curr_guard_row == guard_row:
        if isSafe(curr_guard_row, curr_guard_col, data):
            dist+=1
            if data[guard_row][guard_col] != "X":                
                total += 1
                data[guard_row][guard_col] = "X"
            guard_col -= 1
            curr_guard_col -=1
            continue
        else:
            curr_guard_row = guard_row-1
            curr_guard_col = guard_col
            continue
    elif curr_guard_col == guard_col+1 and curr_guard_row == guard_row:
        if isSafe(curr_guard_row, curr_guard_col, data):
            dist+=1
            if data[guard_row][guard_col] != "X":                
                total += 1
                data[guard_row][guard_col] = "X"
            guard_col += 1
            curr_guard_col +=1
            continue
        else:
            curr_guard_row = guard_row+1
            curr_guard_col = guard_col
            continue

print(total)
# 5086
print(dist)

data = open('D6.txt', "r").read()
temp_data = data.replace("\n", "")
tot_idx = temp_data.index("^")
data = [list(i) for i in data.split("\n")]
guard_row = tot_idx//len(data[0])
guard_col = tot_idx%len(data[0])
# print(guard_row, guard_col)
curr_guard_row = guard_row -1
curr_guard_col = guard_col
store_guard_row = guard_row
store_guard_col = guard_col
store_curr_gurad_row = curr_guard_row
store_curr_gurad_col = curr_guard_col

check=0
obs = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        check = 0
        new_data = copy.deepcopy(data)
        guard_row = store_guard_row
        guard_col = store_guard_col
        curr_guard_row = store_curr_gurad_row
        curr_guard_col = store_curr_gurad_col
        if new_data[i][j] == "#":
            continue
        new_data[i][j] = "#"

        # for k in new_data:
        #     print(k)
        # print()
        while True:

            if curr_guard_row < 0 or curr_guard_col < 0 or curr_guard_row >= len(data) or curr_guard_col >= len(data[0]):
                # print(i,j)
                # for k in new_data:
                #     print(k)
                # print()
                break
            if check > 2*dist:
                # print("here")
                obs+=1
                break
            if curr_guard_col == guard_col and curr_guard_row == guard_row-1:
                if isSafe(curr_guard_row, curr_guard_col, new_data):              
                    # dist+=1
                    # print("here")
                    check+=1
                    if new_data[guard_row][guard_col] != "X":                
                        # total += 1
                        
                        new_data[guard_row][guard_col] = "X"
                    guard_row -= 1
                    curr_guard_row -=1
                    continue
                    
                else:
                    curr_guard_row = guard_row
                    curr_guard_col = guard_col+1
                    continue

            elif curr_guard_col == guard_col and curr_guard_row == guard_row+1:
                if isSafe(curr_guard_row, curr_guard_col, new_data):
                    # dist+=1
                    check+=1
                    if new_data[guard_row][guard_col] != "X": 
                                       
                        # total += 1
                        new_data[guard_row][guard_col] = "X"
                    guard_row += 1
                    curr_guard_row +=1
                    continue
                else:
                    curr_guard_row = guard_row
                    curr_guard_col = guard_col-1
                    continue
            elif curr_guard_col == guard_col-1 and curr_guard_row == guard_row:
                if isSafe(curr_guard_row, curr_guard_col, new_data):
                    # dist+=1
                    check+=1
                    if new_data[guard_row][guard_col] != "X": 
                                       
                        # total += 1
                        new_data[guard_row][guard_col] = "X"
                    guard_col -= 1
                    curr_guard_col -=1
                    continue
                else:
                    curr_guard_row = guard_row-1
                    curr_guard_col = guard_col
                    continue
            elif curr_guard_col == guard_col+1 and curr_guard_row == guard_row:
                if isSafe(curr_guard_row, curr_guard_col, new_data):
                    # dist+=1
                    check+=1
                    if new_data[guard_row][guard_col] != "X": 
                                      
                        # total += 1
                        new_data[guard_row][guard_col] = "X"
                    guard_col += 1
                    curr_guard_col +=1
                    continue
                else:
                    curr_guard_row = guard_row+1
                    curr_guard_col = guard_col
                    continue
            
            
print(obs)
# 1770