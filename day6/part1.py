#!/usr/bin/python

LIGHTS = set()


def turn_on(src_coord, dst_coord):
    for x in range(src_coord[0], dst_coord[0] + 1):
        for y in range(src_coord[1], dst_coord[1] + 1):
            LIGHTS.add((x, y))


def turn_off(src_coord, dst_coord):
    for x in range(src_coord[0], dst_coord[0] + 1):
        for y in range(src_coord[1], dst_coord[1] + 1):
            if (x, y) in LIGHTS:
                LIGHTS.remove((x, y))
            

def toggle(src_coord, dst_coord):
    for x in range(src_coord[0], dst_coord[0] + 1):
        for y in range(src_coord[1], dst_coord[1] + 1):
            if (x, y) in LIGHTS:
                LIGHTS.remove((x, y))
            else:
                LIGHTS.add((x, y))


if __name__ == "__main__":
    with open('input', 'r') as f:
        for line in f:
            instructions = line.replace('\n', '').split(' ')

            action = instructions[0]
            if action == 'turn':
                src_coord = map(int, instructions[2].split(','))
                dst_coord = map(int, instructions[4].split(','))

                if instructions[1] == 'on':
                    turn_on(src_coord, dst_coord)

                else:
                    turn_off(src_coord, dst_coord)
            elif action == 'toggle':
                src_coord = map(int, instructions[1].split(','))
                dst_coord = map(int, instructions[3].split(','))
                toggle(src_coord, dst_coord)

    print len(LIGHTS)
