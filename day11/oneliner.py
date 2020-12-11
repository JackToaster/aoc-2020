# TODO Everything is broken :(
raw_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

input_arr = [list(l) for l in open('input.txt').readlines()]

input_arr = [list(l) for l in raw_input.splitlines()]


count = lambda line, char, input: sum(sum(input[line+dy][char+dx] == '#' for dy in range(-1,2) if (dx!=0|dy==0)&0<=char+dx<len(input[0])&0<=line+dy<len(input)) for dx in range(-1,2))

iteration = lambda input_array: \
[[
    '.' if input_arr[line][character] == '.' else '#' if count(line, character, input_arr) == 0 else 'L' if count(line, character, input_arr) >= 4 else input_arr[line][character]
    for character in range(len(input_arr[0]))
] for line in range(len(input_arr))]

print(
    ''.join(map(lambda l: ''.join(l), (stabilize := lambda f, inputs: inputs if inputs == (outputs := f(input_arr)) else stabilize(f, outputs))(iteration, input_arr)))\
    .count('#')
)

out = (stabilize := lambda f, inputs: inputs if inputs == (outputs := f(input_arr)) else stabilize(f, outputs))(iteration, input_arr)
for line in out:
    print(''.join(line))