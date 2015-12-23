#!/usr/bin/python


def has_two_letter_pair(string):
    letters = list(string)
    lett_length = len(letters)

    for i in range(lett_length - 1):
        if i + 1 <= lett_length - 1:
            pair1 = '{}{}'.format(letters[i], letters[i + 1])
            for j in range(lett_length - 1):
                if j + i + 3 <= lett_length - 1:
                    pair2 = '{}{}'.format(letters[j + i + 2], letters[j + i + 3])
                    if pair1 == pair2:
                        return True

  
def has_repeated_letter(string):
    letters = list(string)
    lett_length = len(letters)

    for i in range(lett_length - 1):
        if i + 2 <= lett_length - 1:
            if letters[i] == letters[i + 2]:
                return True


if __name__ == "__main__":
    nice_strings = 0
    with open('input', 'r') as f:
        for line in f:
            if has_two_letter_pair(line) and has_repeated_letter(line):
                nice_strings += 1
    print nice_strings
