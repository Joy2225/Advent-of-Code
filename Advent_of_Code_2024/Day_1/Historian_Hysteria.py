# Part 1
with open("D1.txt", "r") as f:
    data = f.read().splitlines()
    a, b = sorted([int(i.split()[0]) for i in data]), sorted([int(i.split()[1]) for i in data])
    print(sum([abs(a[i] - b[i]) for i in range(len(a))]))

# 2166959

# Part 2
def make_dict(data):
    c = {}
    for i in data:
        if i not in c:
            c[i] = 1
        else:
            c[i] += 1
    return c
with open("D1.txt", "r") as f:
    data = f.read().splitlines()
    data_0 = [int(i.split()[0]) for i in data]
    data_1 = [int(i.split()[1]) for i in data]
    a = make_dict(data_0)
    b = make_dict(data_1)
    # print(a)
    # print(b)
    print(sum([a[i] * i * b[i] for i in a.keys() if i in b.keys()]))

# 23741109