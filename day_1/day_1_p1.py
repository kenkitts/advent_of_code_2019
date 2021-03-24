from pprint import pprint as pp

with open('input.txt', 'rt') as f:
    inputs = [int(i.strip()) for i in f.readlines()]

total = 0

for i in inputs:
    total += (i // 3) - 2

pp(inputs)
pp(total)


