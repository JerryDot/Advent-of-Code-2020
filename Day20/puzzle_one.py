"""
Tile 1171:
        0
    .##...#...
    .........#
    ....##....
    #.#...##.#
    .....#....
3   .#...#...#  1
    ###.......
    .#........
    #........#
    #..##.##.#
        2
"""
with open("day_twenty.txt", 'r') as puzzle_input:
    raw_tiles = puzzle_input.read().split("\n\n")

tiles = dict()
for raw_tile in raw_tiles:
    split_tile = raw_tile.split(":\n")
    tiles[split_tile[0][-4:]] = list(map(list, split_tile[1].split("\n")))


def binary_to_int(list, one_c="#", zero_c="."):
    x = "".join(list).replace(one_c, "1").replace(zero_c, "0")
    return int(x, 2)


def int_to_bin10(integer):
    string = format(integer, 'b')
    corrected_string = "0" * (10 - len(string)) + string
    return corrected_string

def reverse_bin_value(integer):
    binary_string = int_to_bin10(integer)
    reversed_string = binary_string[::-1]
    return int(reversed_string, 2)

print(reverse_bin_value(256))


list_1 = [".", ".", "#"]
list_2 = ["#", ".", "."]
print(binary_to_int(list_1) == 7 - binary_to_int(list_2))


tiles_numbers = dict()
for slate in tiles:
    tile_array = tiles[slate]
    right_side = [row[9] for row in tile_array]
    left_side = list(reversed([row[0] for row in tile_array]))
    tiles_numbers[slate] = [binary_to_int(tile_array[0])]
    tiles_numbers[slate].append(binary_to_int(right_side))
    tiles_numbers[slate].append(binary_to_int(list(reversed(tile_array[9]))))
    tiles_numbers[slate].append(binary_to_int(left_side))

print(tiles_numbers)
tile_side_counts = dict()
for tile in tiles_numbers:
    counts = []
    for number in tiles_numbers[tile]:
        total = 0
        for tile_tile in tiles_numbers:
            if number in tiles_numbers[tile_tile] or reverse_bin_value(number) in tiles_numbers[tile_tile]:
                total += 1
        counts.append(total)
    tile_side_counts[tile] = counts

product = 1
for tile in tile_side_counts:
    if tile_side_counts[tile].count(1) == 2 and tile_side_counts[tile].count(2) == 2:
        product *= tile
        print(f"tile: {tile}, counts = {tile_side_counts[tile]}, side_numbers = {tiles_numbers[tile]}, tile = {tiles[tile]}")

print(product)
print(tile_side_counts)