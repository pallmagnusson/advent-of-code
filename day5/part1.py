#!/usr/bin/python

ALLOWED = ['a', 'e', 'i', 'o', 'u']
DISALLOWED = ['ab', 'cd', 'pq', 'xy']

nice_strings = 0
with open('input', 'r') as f:
    for line in f:
        allowed_count = 0
        for letter in ALLOWED:
            if letter in line:
                allowed_count += 1

        has_double_letter = False
        letters = list(line)[:-1]
        for index, letter in enumerate(letters):
            if index > 0:
                if letter == letters[index - 1]:
                    has_double_letter = True
                    break

        contains_disallowed = False
        for item in DISALLOWED:
            if item in line:
                contains_disallowed = True
                break

        if allowed_count > 2 and has_double_letter and not contains_disallowed:
            nice_strings += 1
            
print nice_strings
