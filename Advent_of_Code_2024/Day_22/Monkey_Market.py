from collections import defaultdict
data = open("D22.txt").read().splitlines()

def calc_price(price):
    price1 = ((price << 6) ^ price) & 16777215
    price2 = (price1 >> 5 ^ price1) & 16777215
    price3 = ((price2 << 11) ^ price2) & 16777215
    return price3

sum = 0
ans2 = defaultdict(int)
for i in data:
    seen = set()
    tot = 0
    c= int(i)
    num = [c]
    for j in range(2000):
        tot = calc_price(c)
        num.append(tot)
        c = tot
    diff = [num[i]%10-num[i-1]%10 for i in range(1, len(num))] #

    for j in range(0, len(num)-4):
        if tuple(diff[j:j+4]) not in seen:
            ans2[tuple(diff[j:j+4])] += num[j+4]%10
            seen.add(tuple(diff[j:j+4]))
        
    sum += tot
    # print(tot)
print(sum)
#15335183969
print(max(ans2.values()))
#1696