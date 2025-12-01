import re

# Part 1
with open("./D3.txt", "r") as f:
    data = f.read()
all = re.findall(r"mul\((\d+),(\d+)\)", data)
# print(all)
print(sum([int(x) * int(y) for x, y in all]))
# 185797128

# Part 2
with open("./D3.txt", "r") as f:
    data = f.read()
all = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", data)
t = 0
sum = 0
for i in all:
    if i == "don't()":
        t=1
        continue
    elif i == "do()":
        t=0
        continue
    else:
        if t==0:
            temp = re.findall(r"mul\((\d+),(\d+)\)", i)
            # print(temp)
            sum += int(temp[0][0]) * int(temp[0][1])
print(sum)
# 89798695