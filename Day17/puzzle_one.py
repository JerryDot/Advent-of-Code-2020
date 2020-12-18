"""
.#..####
.#.#...#
#..#.#.#
###..##.
..##...#
..##.###
#.....#.
..##..##
"""

import copy

with open("day_seventeen.txt", 'r') as puzzle_input:
    grid = [list(line) for line in puzzle_input.read().split("\n")]

print(grid)

container = [[['.'] * 20] * 20] * 13
real_container = copy.deepcopy(container)
print(real_container)
print(len(real_container))
print(len(real_container[0]))
print(len(real_container[0][0]))

for y, row in enumerate(grid):
    for x, cube in enumerate(row):
        real_container[7][y + 6][x + 6] = cube

print(real_container)
print(real_container[7])
print(real_container[0])


def count_active(pocket_dimension):
    f