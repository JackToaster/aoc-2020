raw_input = open('input.txt').read()


input_lines = raw_input.splitlines()

types = {}


total = 0
for line in input_lines:
    bag_col = line.split(" bags contain ")[0]
    contents = line.split(" bags contain ")[1]
    if contents == "no other bags.":
        types[bag_col] = ['']
    else:
        contents = contents.split(", ")
        types[bag_col] = []
        for content in contents:
            for i in range(int(content[0])):
                types[bag_col].append(content[2:].replace(" bags", "").replace(" bag", "").replace(".", ""))

print(types)


def nesting(type):
    tps = types[type]
    if tps == ['']:
        return 1
    else:
        return sum(nesting(t) for t in tps) + 1


print(nesting("shiny gold") - 1)