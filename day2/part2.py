#!/usr/bin/python

import operator

total = 0

with open('input', 'r') as f:
    for line in f:
        dimensions = map(int, line.split('x'))
        dimensions.sort()
        total += 2 * (dimensions[0] + dimensions[1]) + (reduce(operator.mul, dimensions))

print total
