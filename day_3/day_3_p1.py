from pprint import pprint as pp

with open(file='input.txt', mode='rt') as file:
    lines = [line.strip() for line in file.readlines()]
    line_a, line_b = lines[0].split(','), lines[1].split(',')

grid = {}
pos = [0, 0]

for i in line_a:
    direction = i[0]
    i = int(i.lstrip('UDLR'))
    if direction == 'U':
        for step in range(pos[1], pos[1] + i + 1):
            if grid[(pos[0], step)] is
            grid[(pos[0], step)] = 'a'
            pos[1] = i
    elif direction == 'D':
        pass
    elif direction == 'L':
        pass
    elif direction == 'R':
        pass

pp(grid)

