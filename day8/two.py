raw_input = open('input.txt').read()

input_lines = raw_input.splitlines()

def execute(program):
    acc = 0
    ptr = 0
    visited = []
    while True:
        if ptr in visited:
            return None
        if ptr >= len(program):
            return acc
        visited.append(ptr)
        instruction = program[ptr]
        opcode = instruction[:3]
        operand = instruction[4:]
        if opcode == "acc":
            acc += int(operand)
            ptr += 1
        elif opcode == "nop":
            ptr += 1
        elif opcode == "jmp":
            ptr += int(operand)


for idx, line in enumerate(input_lines):
    if "jmp" in line:
        input_lines[idx] = "nop" + line[3:]
        out = execute(input_lines)
        if out is not None:
            print(out)
        input_lines[idx] = "jmp" + line[3:]
    elif "nop" in line:
        input_lines[idx] = "jmp" + line[3:]
        out = execute(input_lines)
        if out is not None:
            print(out)
        input_lines[idx] = "nop" + line[3:]

