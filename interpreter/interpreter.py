from collections import namedtuple
from typing import List, Optional

raw_input = open('input.txt', 'r').readlines()

Op = namedtuple('Operation', ['op', 'operands'])


def parse_line(line: str) -> Optional[Op]:
    parts = line.split(" ")
    if len(parts) == 1:
        return Op(parts[0], [])
    elif len(parts) > 1:
        return Op(parts[0], parts[1:])
    else:
        print("Empty operation?!")
    return None


def parse(input: List[str]) -> List[Op]:
    program = []
    for idx, line in enumerate(input):
        if parsed_line := parse_line(line):
            program.append(parsed_line)
        else:
            print("Line {} could not be parsed: {}".format(idx, line))
    return program


def execute(program: List[Op], no_loops=False) -> int:
    # Start on first instruction
    instruction_pointer = 0
    acc = 0

    visited = []
    # Continue until
    while 0 <= instruction_pointer < len(program):
        if no_loops and instruction_pointer in visited:
            break
        visited.append(instruction_pointer)
        instruction = program[instruction_pointer]
        op = instruction.op
        operands = instruction.operands

        if op == 'nop':
            pass
        elif op == 'acc':
            acc += int(operands[0])
        elif op == 'jmp':
            instruction_pointer += int(operands[0])
            continue

        # Go to next instruction
        instruction_pointer += 1

    if instruction_pointer < 0:
        print("Instruction pointer negative?!")

    return acc


def evaluate(input: List[str], **kwargs) -> int:
    return execute(parse(input), *kwargs)


print(evaluate(raw_input, no_loops=True))
