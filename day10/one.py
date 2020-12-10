raw_input = open('input.txt').read()

input_lines = sorted([int(l) for l in raw_input.splitlines()])

ones = 0
threes = 0
last_joltage = 0
for line in input_lines:
    if line - last_joltage == 1:
        ones += 1
    elif line - last_joltage == 3:
        threes += 1
    else:
        print(line - last_joltage)

    last_joltage = line

print(ones, threes + 1)
