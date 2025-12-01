import re
towel = open("D19.txt").read().split("\n\n")[0].replace(" ", "").split(",")
lines = open("D19.txt").read().split("\n\n")[1].split("\n")
pattern_cache = dict()

def pattern(line):
    if line == "":
        return 1

    if line in pattern_cache:
        return pattern_cache[line]

    matches = 0
    for t in towel:
        if re.search('^' + t, line):
            new_pattern = line[len(t):]
            matches += pattern(new_pattern)
    pattern_cache[line] = matches
    return matches

c1 = 0
c2 = 0
for p in lines:
    temp_counter = pattern(p)
    if temp_counter:
        c1 += 1
        c2 += temp_counter

print(c1)
# 374
print(c2)
# 1100663950563322