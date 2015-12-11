#!/usr/bin/python

total = 0

with open('input', 'r') as f:
    for line in f:
        length, width, height = map(int, line.split('x'))
        areas = [length * width, width * height, height * length]
        total += sum([2 * area for area in areas]) + min(areas)

print total
