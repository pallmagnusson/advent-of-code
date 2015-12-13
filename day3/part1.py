#!/usr/bin/python

NORTH = '^'
SOUTH = 'v'
EAST = '>'
WEST = '<'

with open('input', 'r') as f:
    directions = list(f.read())[:-1]

route = [[0, 0]]
houses = 1
for index, direction in enumerate(directions):
    last_x_pos = route[-1][0]
    last_y_pos = route[-1][1]

    if direction == NORTH:
        new_pos = [last_x_pos, last_y_pos + 1]

    if direction == SOUTH:
        new_pos = [last_x_pos, last_y_pos - 1]

    if direction == EAST:
        new_pos = [last_x_pos + 1, last_y_pos]

    if direction == WEST:
        new_pos = [last_x_pos - 1, last_y_pos]

    if new_pos not in route:
        houses += 1

    route.append(new_pos)

print houses
