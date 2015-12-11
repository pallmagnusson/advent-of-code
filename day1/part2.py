#!/usr/bin/python

with open('input', 'r') as f:
    instructions = f.read()

UP = '('
DOWN = ')'

floor = 0
for index, action in enumerate(instructions):
    if action == UP:
        floor += 1
    elif action == DOWN:
        floor -= 1

    if floor == -1:
        print index + 1
        break
