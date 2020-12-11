raw_input = open('input.txt').read()

input_lines = [list(l) for l in raw_input.splitlines()]

def is_occupied(x, y, inp):
    if y < 0 or x < 0:
        return False
    try:
        return inp[y][x] == '#'
    except Exception:
        return False

def num_neighbors(x, y, inp):
    num = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                num += int(is_occupied(x+i, y+j, inp))

    return num

import copy
def iteration(input):
    new_input = copy.deepcopy(input)

    for y in range(len(input)):
        for x in range(len(input[0])):
            char = input[y][x]
            if char == 'L' and num_neighbors(x, y, input) == 0:
                new_input[y][x] = '#'
            elif char == '#' and num_neighbors(x,y,input) >= 4:
                new_input[y][x] = 'L'

    return new_input


ans = 0
for i in range(100):
    new_input_lines = iteration(input_lines)
    if new_input_lines == input_lines:
        ans = ''.join(''.join(l) for l in new_input_lines).count('#')
        break
    input_lines = new_input_lines
print(ans)