
def find_trees(x_increment, y_increment):
    with open("day_three.txt", 'r') as puzzle_input:
        input_list = puzzle_input.readlines()
        tree_count = 0
        horizontal_position = 0

        for vert, line in enumerate(input_list):
            if vert % y_increment == 0:
                if line[horizontal_position] == "#":
                    tree_count += 1
                horizontal_position += x_increment
            horizontal_position %= 31

        return tree_count

print(find_trees(3,1))
answer = 1
patterns_to_check = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for pattern in patterns_to_check:
    answer *= find_trees(pattern[0], pattern[1])
print(answer)