schematics = [schematic.split() for schematic in open("D25.txt").read().split('\n\n')]

locks = []
for schematic in schematics:
    if '.' not in schematic[0]:
        lock = []
        for i in range(5):
            count = sum([1 for j in range(7) if schematic[j][i] == '#']) - 1
            lock.append(count)
        locks.append(lock)

keys = []
for schematic in schematics:
    if '.' not in schematic[-1]:
        key = []
        for i in range(5):
            count = sum([1 for j in range(7) if schematic[j][i] == '#']) - 1
            key.append(count)
        keys.append(key)

count = 0
for lock in locks:
    for key in keys:
        if sum([1 for column in zip(lock, key) if sum(column) > 5]) == 0:
            count += 1

print(count)