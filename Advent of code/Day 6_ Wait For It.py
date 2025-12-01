import re
with open('D6.txt','r') as file:
    values=file.read().split('\n')

# part 1
time=re.findall(r'\d+', values[0])
time=list(map(int,time))

distance=re.findall(r'\d+', values[1])
distance=list(map(int,distance))

prod=1
for index,tim in enumerate(time):
    count=0
    for i in range(tim+1):
        dist=i*(tim-i)
        if dist > distance[index]:
            count+=1
    prod*=count

print(prod)

# part 2
time=int(''.join(i for i in (re.findall(r'\d',values[0]))))
distance=int(''.join(i for i in (re.findall(r'\d',values[1]))))

count=0
for i in range(time+1):
    dist=i*(time-i)
    if dist > distance:
        count+=1

print(count)
