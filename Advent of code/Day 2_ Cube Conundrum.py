from numpy import prod
with open('D2.txt','r') as file:
    values=file.read().replace(':',';').split('\n')

# part 1
sum=0
for i,s in enumerate(values):
    _, *s=s.split(';')
    c=0
    for val in s:
        if('red' in val):
            if(not int( val [val.index('red')-2::-1].split()[0][::-1] ) <= 12 ):
                c=1
                break
        if('green' in val):
            if(not int( val [val.index('green')-2::-1].split()[0][::-1] ) <= 13 ):
                c=1
                break
        if('blue' in val):
            if(not int( val [val.index('blue')-2::-1].split()[0][::-1] ) <= 14 ):
                c=1
                break
    if not c==1:
        sum=sum+i+1
print(sum)

# part 2
sum=0
for i,s in enumerate(values):
    _, *s=s.split(';')
    c=0
    max=[0,0,0]
    for val in s:
        if('red' in val):
            if( int((val[val.index('red')-2::-1].split()[0])[::-1]) > max[0] ):
                max[0] = int(val[val.index('red')-2::-1].split()[0][::-1])
        if('green' in val):
            if( int((val[val.index('green')-2::-1].split()[0])[::-1]) > max[1]):
                max[1] = int(val[val.index('green')-2::-1].split()[0][::-1])
        if('blue' in val):
            if( int((val[val.index('blue')-2::-1].split()[0])[::-1]) > max[2]):
                max[2] = int(val[val.index('blue')-2::-1].split()[0][::-1])
    sum=sum+prod(max)
print(sum)