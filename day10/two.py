from functools import lru_cache

import networkx as nx

import matplotlib.pyplot as plt
from math import floor, ceil
raw_input = open('input.txt').read()

input_lines = sorted([int(l) for l in raw_input.splitlines()] + [0])
print(input_lines)


@lru_cache(maxsize=32)
def count_paths(num_ones):
    if num_ones <= 1:
        return 1
    graph = nx.DiGraph()
    for node in range(num_ones):
        graph.add_node(node)
        if node > 0:
            graph.add_edge(node-1, node)
        if node > 1:
            graph.add_edge(node-2, node)
        if node > 2:
            graph.add_edge(node-3, node)

    # nx.draw(graph)
    # plt.show()
    paths = nx.all_simple_paths(graph, 0, num_ones - 1)
    return len(list(paths))


path_count = 1
ones_in_a_row = 0
for line in input_lines:
    if line - 1 in input_lines:
        ones_in_a_row += 1
    else:
        print(ones_in_a_row, count_paths(ones_in_a_row))
        path_count *= count_paths(ones_in_a_row)
        ones_in_a_row = 1

print(path_count * count_paths(ones_in_a_row))
