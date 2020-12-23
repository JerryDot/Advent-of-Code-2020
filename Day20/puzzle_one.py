"""
example tile:
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


def create_tile_no_dict(tile_dict):
    tiles_numbers = dict()
    for slate in tile_dict:
        tile_array = tiles[slate]
        right_side = [row[9] for row in tile_array]
        left_side = list(reversed([row[0] for row in tile_array]))
        tiles_numbers[slate] = [binary_to_int(tile_array[0])]
        tiles_numbers[slate].append(binary_to_int(right_side))
        tiles_numbers[slate].append(binary_to_int(list(reversed(tile_array[9]))))
        tiles_numbers[slate].append(binary_to_int(left_side))
    return tiles_numbers


def create_tiles_dict(raw_tile_list):
    tile_dict = dict()
    for raw_tile in raw_tile_list:
        split_tile = raw_tile.split(":\n")
        tile_dict[split_tile[0][-4:]] = list(map(list, split_tile[1].split("\n")))
    return tile_dict


tiles = create_tiles_dict(raw_tiles)
tile_sides = create_tile_no_dict(tiles)


tile_side_counts = dict()
for tile in tile_sides:
    counts = []
    for number in tile_sides[tile]:
        total = 0
        for tile_tile in tile_sides:
            if number in tile_sides[tile_tile] or reverse_bin_value(number) in tile_sides[tile_tile]:
                total += 1
        counts.append(total)
    tile_side_counts[tile] = counts

product = 1
for tile in tile_side_counts:
    if tile_side_counts[tile].count(1) == 2 and tile_side_counts[tile].count(2) == 2:
        product *= tile
        print(f"tile: {tile}, counts = {tile_side_counts[tile]}, side_numbers = {tile_sides[tile]}, tile = {tiles[tile]}")

print(f"Answer is {product}")