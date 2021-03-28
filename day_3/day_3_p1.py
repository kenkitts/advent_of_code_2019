from pprint import pprint as pp

with open(file='input.txt', mode='rt') as file:
    lines = [line.strip() for line in file.readlines()]
    line_a, line_b = lines[0].split(','), lines[1].split(',')

grid_a = []
grid_b = []
pos_a = [0, 0]
pos_b = [0, 0]

for i in line_a:
    direction = i[0]
    i = int(i.lstrip('UDLR'))
    if direction == 'U':
        for step in range(pos_a[1], pos_a[1] + i + 1):
            grid_a.append((pos_a[0], step))
        pos_a[1] = pos_a[1] + i
    elif direction == 'D':
        for step in range(pos_a[1], pos_a[1] - i - 1, -1):
            grid_a.append((pos_a[0], step))
        pos_a[1] = pos_a[1] - i
    elif direction == 'L':
        for step in range(pos_a[0], pos_a[0] - i - 1, -1):
            grid_a.append((step, pos_a[1]))
        pos_a[0] = pos_a[0] - i
    elif direction == 'R':
        for step in range(pos_a[0], pos_a[0] + i + 1):
            grid_a.append((step, pos_a[1]))
        pos_a[0] = pos_a[0] + i
grid_a.remove((0, 0))

for i in line_b:
    direction = i[0]
    i = int(i.lstrip('UDLR'))
    if direction == 'U':
        for step in range(pos_b[1], pos_b[1] + i + 1):
            grid_b.append((pos_b[0], step))
        pos_b[1] = pos_b[1] + i
    elif direction == 'D':
        for step in range(pos_b[1], pos_b[1] - i - 1, -1):
            grid_b.append((pos_b[0], step))
        pos_b[1] = pos_b[1] - i
    elif direction == 'L':
        for step in range(pos_b[0], pos_b[0] - i - 1, -1):
            grid_b.append((step, pos_b[1]))
        pos_b[0] = pos_b[0] - i
    elif direction == 'R':
        for step in range(pos_b[0], pos_b[0] + i + 1):
            grid_b.append((step, pos_b[1]))
        pos_b[0] = pos_b[0] + i
grid_b.remove((0, 0))

intersect = []

for i in grid_a:
    if i in grid_b:
        intersect.append(i)

pp(intersect)
