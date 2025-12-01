with open('D4.txt','r') as file:
    values=file.read().split('\n')
# part 1
s=0
for val in values:
    c=0
    winnings=val[val.index(':')+1:val.index('|')].strip().replace('  ',' ').split(' ')
    numbers=val[val.index('|')+1:].strip().replace('  ',' ').split(' ')
    c = len(set(numbers) & set(winnings))
    s=s+int(2**(c-1))
print(s)

# part 2
s=0
card_no=[1]*len(values)

for index,val in enumerate(values):
    winnings=val[val.index(':')+1:val.index('|')].strip().replace('  ',' ').split(' ')
    numbers=val[val.index('|')+1:].strip().replace('  ',' ').split(' ')
    c = len(set(numbers) & set(winnings))
    #print(card_no)  
    for i in range(index+1, index+c+1):
        card_no[i]=card_no[i]+1*card_no[index]
s=sum(card_no)
print(s)