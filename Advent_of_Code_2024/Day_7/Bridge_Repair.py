import itertools
data = open("D7.txt", "r").read().splitlines()
val = [int(i[:i.index(":")]) for i in data]
elements, operator = [list(map(int, ( i[i.index(":")+2 : ]).split(" "))) for i in data], '+*|'
total=0
for i,value in enumerate(val):
    print("Line " , i+1)
    length = len(elements[i])
    perm = list(itertools.product(operator, repeat = length-1))
    c = str(elements[i].pop(0)) # used to store the first element
    for p in perm:
        temp_str = c
        sol = 0
        for k,l in zip(elements[i], p):
            if l=='|':
                temp_str+=str(k)
                sol = temp_str
                continue
            temp_str+=l+str(k)
            sol = eval(temp_str)
            temp_str = str(sol)
        if int(temp_str)==value:
            total+=value
            break

print(total)
# Part 1 :- 2501605301465
# Part 2 :- 44841372855953