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
        types[bag_col] = [content[2:].replace(" bags", "").replace(" bag", "").replace(".", "") for content in contents]


def get_contents(type):
    tps = types[type]
    if "shiny gold" in tps:
        return True
    if tps == ['']:
        return False
    else:
        return any(get_contents(t) for t in tps)


for type in types:
    total += int(get_contents(type))

print(total)