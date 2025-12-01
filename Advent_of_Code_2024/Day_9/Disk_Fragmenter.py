# Part 1
import time
s = time.time()
data = open("D9.txt", "r").read()
dotted_rep = []

c = 0
for i, j in enumerate(data):
    if i % 2 == 0:
        dotted_rep += [str(c)] * int(j)
        c+=1
    else:
        dotted_rep += ['.'] * int(j)

idx1, idx2 = dotted_rep.index('.'), len(dotted_rep) - 1

while idx1 < idx2:
    dotted_rep[idx1], dotted_rep[idx2] = dotted_rep[idx2], dotted_rep[idx1]
    idx1 += 1
    idx2 -= 1
    while dotted_rep[idx1] != '.':
        idx1 += 1
    while dotted_rep[idx2] == '.':
        idx2 -= 1

dotted_rep = dotted_rep[:dotted_rep.index('.')]


sum = 0
for i in range(0, len(dotted_rep)):
    sum += int(dotted_rep[i])*i
print(sum)
# 6279058075753

# Part 2
data = open("D9.txt", "r").read()
dotted_rep = []

c = 0
count = 0
for i, j in enumerate(data):
    if i % 2 == 0:
        dotted_rep+=[[str(c)] * int(j)] 
        c+=1
    else:
        if j !='0':
            dotted_rep+=[['.'] * int(j)]

dot_map = {tuple(i) for i in dotted_rep if '.' in i}
# dot_idx = [dotted_rep.index(i) for i in dot_map if '.' in i]
block_map = [i for i in dotted_rep if '.' not in i][::-1]
dot_map_ea_len = [len(i) for i in dot_map]

# print(dotted_rep)

for idx,i in enumerate(block_map):
    # print("Index:-",str(idx))
    file_len = len(i)
    t=0
    # start=0
    for k in range(len(dot_map_ea_len)):
        if dot_map_ea_len[k] >= file_len:
            t=1
            # start=k
            break
    if not t:
        continue  
    min_dot_tuple = min( # Find the dot tuple which stisfies the condition and has the least index
        (j for j in dot_map if dotted_rep.index(list(j)) < dotted_rep.index(i) and len(j) >= len(i)),
        key=lambda x: dotted_rep.index(list(x)),
        default=None
    )
    if min_dot_tuple is None:
        continue
    # min_dot_tuple = min(dot_map, key=lambda x: dotted_rep.index(list(x)))
    # for j in dot_map:
    dot_len = len(min_dot_tuple)
    
    # if dotted_rep.index(list(j)) < dotted_rep.index(i) and dot_len >= len(i):
    count+=1


    if dot_len > len(i):
        c=1

    dotted_rep[dotted_rep.index(i)], dotted_rep[dotted_rep.index(list(min_dot_tuple))] = ['.'] * len(i), i

    if c==1:
        if len(['.'] * ( dot_len - len(i) )):
            dotted_rep.insert(dotted_rep.index(i)+1, ['.'] * ( dot_len - len(i) ))
            dot_map.add( tuple(['.'] * (dot_len - len(i))))

sum = 0
c = 0
for val in dotted_rep:
    for val1 in val:
        if val1 != '.':
            sum += int(val1)*c
        c+=1
print(sum)
# 6301361958738
f = time.time()
print("Time Taken:-",f-s)
# Time Taken:- 19.383069038391113 seconds After messing with it for around 6 hrs