#!/usr/bin/python

ALLOWED = ['a', 'e', 'i', 'o', 'u']
DISALLOWED = ['ab', 'cd', 'pq', 'xy']


def has_allowed_count(line):
    allowed_count = 0
    for letter in list(line):
        if letter in ALLOWED:
            allowed_count += 1
    if allowed_count > 2:
        return True
    return False


def has_double_letter(line):
    letters = list(line)[:-1]
    for index, letter in enumerate(letters):
        if index > 0:
            if letter == letters[index - 1]:
                return True
    return False


def has_disallowed(line):
    for item in DISALLOWED:
        if item in line:
            return True
    return False


if __name__ == "__main__":
    nice_strings = 0
    with open('input', 'r') as f:
        for line in f:
            if has_allowed_count(line) and has_double_letter(line) and not has_disallowed(line):
                nice_strings += 1
    print nice_strings
