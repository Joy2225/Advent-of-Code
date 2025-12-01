from itertools import cycle
from re import match

with open('D8.txt') as file:
    steps, _, *nodes = file.read().split('\n')

# Part 1
    
instructions = cycle(map('LR'.index, steps))
node_map = {}

for node in nodes:
    cnode, lnode, rnode = match(r'(...) = \((...), (...)\)', node).groups()
    node_map[cnode] = [lnode, rnode]

node, stepss = 'AAA', 0
while node != 'ZZZ':
    node = node_map[node][next(instructions)]
    stepss += 1

print(stepss)

# Part 2

from math import lcm



node_map = {}

for node in nodes:
    cnode, lnode, rnode = match(r'(...) = \((...), (...)\)', node).groups()
    node_map[cnode] = [lnode, rnode]


def get_required(node):
    tsteps, instructions = 0, cycle(map('LR'.index, steps))
    while node[-1] != 'Z':
        node = node_map[node][next(instructions)]
        tsteps += 1
    return tsteps


nodes = [node for node in node_map if node[-1] == "A"]
print(lcm(*map(get_required, nodes)))
