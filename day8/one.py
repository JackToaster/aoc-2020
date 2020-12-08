raw_input = open('input.txt').read()

input_lines = raw_input.splitlines()


def execute(program):
    acc = 0
    ptr = 0
    visited = []
    while True:
        if ptr in visited:
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


print(execute(input_lines))
