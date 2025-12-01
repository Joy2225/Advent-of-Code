def check_pages(line, dic) -> bool:
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            if line[i] in dic.keys():
                if line[j] in dic[line[i]]:
                    continue
                else:
                    if line[i] in dic[line[j]]:
                        return False
            else:
                if line[j] in dic.keys():
                    if line[i] in dic[line[j]]:
                        return False

    return True

# Part 1

with open("D5.txt", 'r') as file:
    data = file.read().split("\n\n")
page_com = data[0].split("\n")
pages = [list(map(int, i.split(','))) for i in data[1].split("\n")]
dic = {} 

for i in range(len(page_com)):
    dic[int(page_com[i][:2])] = []
for i in range(len(page_com)):
    dic[int(page_com[i][:2])].append(int(page_com[i][3:]))

total = 0
wrong = []
for i in pages:
    if check_pages(i, dic):
        # print(i)
        total += i[len(i)//2]
    else:
        wrong.append(i)
print(total)
# 4637

# Part 2
def find_wrong(wrong, dic):
     for i in range(len(wrong)-1):
        for j in range(i+1, len(wrong)):
            if wrong[i] in dic.keys():
                if wrong[j] in dic[wrong[i]]:
                    continue
                else:
                    if wrong[i] in dic[wrong[j]]:
                        wrong[i], wrong[j] = wrong[j], wrong[i]
                        if check_pages(wrong, dic):
                            return wrong
                        else:
                            return find_wrong(wrong, dic)
            else:
                if wrong[j] in dic.keys():
                    if wrong[i] in dic[wrong[j]]:
                        wrong[i], wrong[j] = wrong[j], wrong[i]
                        if check_pages(wrong, dic):
                            return wrong
                        else:
                            return find_wrong(wrong, dic)
     return wrong

total = 0
for i in wrong:
    temp =  find_wrong(i, dic)
    # print(temp)
    total += temp[len(temp)//2]
print(total)
# 6370
