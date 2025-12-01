from collections import Counter

with open('D7.txt') as file:
    input_data = *map(str.split, file.read().split('\n')),

# Part 1
card_strength = '23456789TJQKA'
total_sum = 0
get_strength = lambda card: (sorted(Counter(card[0]).values())[::-1], *map(card_strength.index, card[0]))

order = sorted(input_data, key=get_strength)
for rank, (_, bid) in enumerate(order, 1):
    total_sum += int(bid) * rank

print(total_sum)

# Part 2

card_strength = 'J23456789TQKA'
total_sum = 0


def get_strength(card):
    counter = sorted(Counter(card[0].replace('J', '')).values(), reverse=True)
    if not len(counter):
        counter = [0]
    counter[0] += card[0].count('J')
    return counter, *map(card_strength.index, card[0])


order = sorted(input_data, key=get_strength)
for rank, (_, bid) in enumerate(order, 1):
    total_sum += int(bid) * rank

print(total_sum)