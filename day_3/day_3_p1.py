import time

start_time = time.time()

with open(file='input.txt', mode='rt') as file:
    lines = [line.strip() for line in file.readlines()]
    line_a, line_b = lines[0].split(','), lines[1].split(',')


def draw_line(line, pos):
    """This function takes two list inputs, 'line' and 'pos'.
    The line input is the list of instructions to execute.
    The pos input is the positional coordinates from where to mapping
    the line to a grid.  The return value is the grid (map)."""
    grid = []
    for i in line:
        direction = i[0]
        i = int(i.lstrip('UDLR'))
        if direction == 'U':
            for step in range(pos[1], pos[1] + i + 1):
                grid.append((pos[0], step))
            pos[1] = pos[1] + i
        elif direction == 'D':
            for step in range(pos[1], pos[1] - i - 1, -1):
                grid.append((pos[0], step))
            pos[1] = pos[1] - i
        elif direction == 'L':
            for step in range(pos[0], pos[0] - i - 1, -1):
                grid.append((step, pos[1]))
            pos[0] = pos[0] - i
        elif direction == 'R':
            for step in range(pos[0], pos[0] + i + 1):
                grid.append((step, pos[1]))
            pos[0] = pos[0] + i
    grid.remove((0, 0))
    return grid


grid_a = draw_line(line_a, [0, 0])
grid_b = draw_line(line_b, [0, 0])
intersect = []
for i in grid_a:
    if i in grid_b:
        intersect.append(i)
closest_intersection = min([i[0] + abs(i[1]) for i in intersect])
stop_time = time.time()
total_time = stop_time - start_time

print('The solution to day 3, part 1 is {}.\nThis program took {} seconds to execute.'
      .format(closest_intersection, total_time))
