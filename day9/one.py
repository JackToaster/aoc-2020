raw_input = open('input.txt').read()

input_lines = [int(l) for l in raw_input.splitlines()]


def twosum(nums, sum):
    for num1 in nums:
        for num2 in nums:
            if num1 + num2 == sum:
                return True
    return  False

for i in range(25, len(input_lines)):
    preamble = input_lines[i-25:i]
    num = input_lines[i]
    if not twosum(preamble, num):
        print(num)


