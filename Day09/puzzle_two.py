
with open("day_nine.txt", 'r') as puzzle_input:
    input_list = list(map(int, puzzle_input.read().split("\n")))

sum_target = 1124361034


def solve_two(input_list, sum_target):
    for index, starting_value in enumerate(input_list):
        running_total = starting_value
        counter = index
        smallest_value = starting_value
        largest_value = starting_value
        while running_total < sum_target:
            counter += 1
            next_number = input_list[counter]
            running_total += next_number
            if next_number < smallest_value:
                smallest_value = next_number
            if next_number > largest_value:
                largest_value = next_number

        if running_total == sum_target:
            return smallest_value + largest_value


print(solve_two(input_list, sum_target))
