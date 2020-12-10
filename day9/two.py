raw_input = open('input.txt').read()

input_lines = raw_input.splitlines()


for size in range(2, len(input_lines)):
    for i in range(len(input_lines) - size):
        if sum(int(l) for l in input_lines[i:i+size]) == 1639024365:
            print(min(int(l) for l in input_lines[i:i+size]) + max(int(l) for l in input_lines[i:i+size]))
