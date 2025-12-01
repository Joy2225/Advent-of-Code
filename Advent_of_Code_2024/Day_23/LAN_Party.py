from itertools import combinations

data = open("D23.txt").read().splitlines()
connection, computer = set(), set()

for i in data:
    a, b = i.split('-')
    computer.update([a,b])
    connection.update([(a,b), (b,a)])

t = []

for a, b, c in combinations(computer, 3):
    if {(a,b), (a,c), (b,c)} < connection and 't' in (a+b+c)[::2]:
        t.append(a)

print(len(t))
# 1238

network = [{c} for c in computer]
for n in network:
    for c in computer:
        if all((c,d) in connection for d in n): 
            n.add(c)

print(*sorted(max(network, key=len)), ',')
# bg,bl,ch,fn,fv,gd,jn,kk,lk,pv,rr,tb,vw