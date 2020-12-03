
with open("day_three.txt", 'r') as puzzle_input:
    tree_count = 0
    horizontal_position = 0

    for line in puzzle_input:
        if line[horizontal_position] == "#":
            tree_count += 1
        horizontal_position += 3
        horizontal_position %= 31

    print(tree_count)
