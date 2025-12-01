# Part 1
with open("D2.txt", "r") as f:
    data = f.read().splitlines()
    safe = 0
    for i in data:
        c=0
        l = list(map(int,i.split()))
        if l == sorted(l) or l == sorted(l, reverse=True):
            for j in range(1, len(l)):
                temp = abs(l[j] - l[j-1])
                if not (temp ==1 or temp==2 or temp==3):
                    c=1
                    break
        else:
            continue
            
        if c == 0:
            safe += 1
    print(safe)
    # 564

# Part 2
def check_list(l):
    c=0
    if l == sorted(l) or l == sorted(l, reverse=True):
            for j in range(1, len(l)):
                temp = abs(l[j] - l[j-1])
                if not (temp ==1 or temp==2 or temp==3):
                    c=1
                    break
    else :
        return False
    if c == 0:
        return True
    return False

def remove_and_check(l):
    for i in range(len(l)):
        temp = l[i]
        l.pop(i)
        if check_list(l):
            return True
        l.insert(i, temp)
    return False        



with open("D2.txt", "r") as f:
    data = f.read().splitlines()
    safe = 0
    for i in data:
        c=0
        l = list(map(int,i.split()))
        if check_list(l) or remove_and_check(l):
            safe += 1
    print(safe)
    # 604