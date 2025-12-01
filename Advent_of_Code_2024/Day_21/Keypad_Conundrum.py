# import re
# data = '''029A
# 980A
# 179A
# 456A
# 379A'''.splitlines()
# keypad =  dict()
# for i, row in enumerate([[7,8,9],[4,5,6],[1,2,3],[-1,0,'A']]):
#     for j,val in enumerate(row):
#         keypad[str(val)] = (i,j)

# remote = dict()
# for i, row in enumerate([['-1', '^', 'A'], ['<', 'v', '>']]):
#     for j, val in enumerate(row):
#         remote[val] = (i,j)


# def robot_keypad(data):
#     start = keypad['A']
#     # count = 0
#     dir = ''
#     for i in data:
#         if start[1] - keypad[i][1] < 0:
#             dir += '>' * abs(start[1] - keypad[i][1])
#         elif start[1] - keypad[i][1] > 0:
#             dir += '<' * abs(start[1] - keypad[i][1])

#         if start[0] - keypad[i][0] < 0:
#             dir += 'v' * abs(start[0] - keypad[i][0])
#         elif start[0] - keypad[i][0] > 0:
#             dir += '^' * abs(start[0] - keypad[i][0])      
        

#         dir += 'A'
#         # count += abs(start[0] - keypad[i][0]) + abs(start[1] - keypad[i][1]) + 1
#         start = keypad[i]
#     # print(dir)
#     return dir

# # print(robot_keypad(data))

# def robot_remote(data):
#     start = remote['A']
#     # count = 0
#     dir = ''
#     for i in data:

#         if start[0] - remote[i][0] < 0:
#             dir += 'v' * abs(start[0] - remote[i][0])
#         elif start[0] - remote[i][0] > 0:
#             dir += '^' * abs(start[0] - remote[i][0])
            
#         if start[1] - remote[i][1] < 0:
#             dir += '>' * abs(start[1] - remote[i][1])
#         elif start[1] - remote[i][1] > 0:
#             dir += '<' * abs(start[1] - remote[i][1])
        
        

#         dir += 'A'    
#         # count += abs(start[0] - remote[i][0]) + abs(start[1] - remote[i][1]) + 1
#         start = remote[i]
#     # print(dir)
#     return dir

# # print(robot_remote(robot_remote(robot_keypad(data))))
# total = 0

# for i in data:
#     print(len(robot_remote(robot_remote(robot_keypad(i)))))
#     print(int(i[:-1]))
#     print(robot_keypad(i))
#     print(robot_remote(robot_keypad(i)))
#     print(robot_remote(robot_remote(robot_keypad(i))))
#     total += len(robot_remote(robot_remote(robot_keypad(i)))) * int(i[:-1])

# print(total)
# This is wrong arghhhhhh

from collections import Counter

codes = open("D21.txt").read().splitlines()

keyp = {c: (i % 3, i // 3) for i, c in enumerate("789456123 0A")}
dirp = {c: (i % 3, i // 3) for i, c in enumerate(" ^A<v>")}


def steps(G, s, i=1):
    px, py = G["A"]
    bx, by = G[" "]
    res = Counter()
    for c in s:
        npx, npy = G[c]
        f = npx == bx and py == by or npy == by and px == bx
        res[(npx - px, npy - py, f)] += i
        px, py = npx, npy
    return res


def go(n):
    r = 0
    for code in codes:
        res = steps(keyp, code)
        for _ in range(n + 1):
            res = sum((steps(dirp, ("<" * -x + "v" * y + "^" * -y + ">" * x)[:: -1 if f else 1] + "A", res[(x, y, f)]) for x, y, f in res), Counter())
        r += res.total() * int(code[:3])
    return r


print(go(2))
print(go(25))
