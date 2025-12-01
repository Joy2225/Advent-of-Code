import re

# Part 1
def check_xmas(a):
    return len(re.findall(r'XMAS', a)+re.findall(r'SAMX', a))

data = open('D4.txt', "r").read().split("\n")
total = 0
total += sum([check_xmas(i) for i in data])
# temp_data = data.split('\n')
top_down = [''.join(data[i][j] for i in range(len(data))) for j in range(len(data[0]))]
# print(top_down)
total += sum([check_xmas(i) for i in top_down])
# print(total)
tl_br = [ ''.join(data[i+x][j+x]for x in range(4)) for i in range(0, len(data)-3) for j in range(0, len(data[i])-3)]
# print(tl_br)
total += tl_br.count('XMAS') + tl_br.count('SAMX')
tr_bl = [ ''.join(data[i+x][j-x]for x in range(4)) for i in range(0, len(data)-3) for j in range(len(data[i])-1,2,-1)]
# print(tr_bl)
total += tr_bl.count('XMAS') + tr_bl.count('SAMX')
print(total)
# 2378


# Part 2
def check_x_mas(data, i, j):
    return ((data[i-1][j-1]=='M' and data[i+1][j+1]=='S') or (data[i-1][j-1]=='S' and data[i+1][j+1]=='M')) and ((data[i-1][j+1]=='M' and data[i+1][j-1]=='S') or (data[i-1][j+1]=='S' and data[i+1][j-1]=='M'))

data = open('D4.txt', "r").read().split("\n")
total = 0
total = sum(1 if data[i][j]=='A' and check_x_mas(data, i, j) else 0 for i in range(1, len(data)-1) for j in range(1, len(data[i])-1))
print(total)
# 1796
