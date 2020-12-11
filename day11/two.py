raw_input = open('input.txt').read()
# raw_input = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""
input_lines = [list(l) for l in raw_input.splitlines()]

def is_seat(x, y, inp):
    if y < 0 or x < 0 or x >= len(inp[0]) or y >= len(inp):
        return False
    try:
        return inp[y][x] == '#' or inp[y][x] == 'L'
    except Exception:
        return False


def is_occupied(x, y, inp):
    if y < 0 or x < 0 or x >= len(inp[0]) or y >= len(inp):
        return False
    try:
        return inp[y][x] == '#'
    except Exception:
        return False

def num_neighbors(x, y, inp):
    num = 0
    for X in range(1, len(inp[0])):
        if is_seat(x+X, y+X, inp):
            num += is_occupied(x+X, y+X, inp)
            break
    for X in range(1, len(inp[0])):
        if is_seat(x - X, y + X, inp):
            num += is_occupied(x - X, y + X, inp)
            break
    for X in range(1, len(inp[0])):
        if is_seat(x + X, y - X, inp):
            num += is_occupied(x + X, y - X, inp)
            break
    for X in range(1, len(inp[0])):
        if is_seat(x - X, y - X, inp):
            num += is_occupied(x - X, y - X, inp)
            break


    for X in range(1, len(inp[0])):
        if is_seat(x - X, y, inp):
            num += is_occupied(x - X, y, inp)
            break
    for X in range(1, len(inp[0])):
        if is_seat(x + X, y, inp):
            num += is_occupied(x + X, y, inp)
            break

    for X in range(1, len(inp[0])):
        if is_seat(x, y - X, inp):
            num += is_occupied(x, y - X, inp)
            break
    for X in range(1, len(inp[0])):
        if is_seat(x, y + X, inp):
            num += is_occupied(x, y + X, inp)
            break

    return num

import copy
def iteration(input):
    new_input = copy.deepcopy(input)

    for y in range(len(input)):
        for x in range(len(input[0])):
            char = input[y][x]
            if char == 'L' and num_neighbors(x, y, input) == 0:
                new_input[y][x] = '#'
            elif char == '#' and num_neighbors(x,y,input) >= 5:
                new_input[y][x] = 'L'

    return new_input


# input_lines = iteration(input_lines)
# input_lines = iteration(input_lines)
#
# print(num_neighbors(3, 0, input_lines))
#
# for line in input_lines:
#     print(''.join(line))

ans = 0
while True:
    new_input_lines = iteration(input_lines)
    if new_input_lines == input_lines:
        ans = ''.join(''.join(l) for l in new_input_lines).count('#')
        break
    input_lines = new_input_lines

# for line in input_lines:
#     print(''.join(line))
print(ans)