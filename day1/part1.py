#!/usr/bin/python

with open('input', 'r') as f:
    instructions = f.read()

UP = '('
DOWN = ')'

print instructions.count(UP) - instructions.count(DOWN)
