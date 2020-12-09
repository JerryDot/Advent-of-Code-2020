import itertools
import collections

with open("day_nine.txt", 'r') as puzzle_input:
    input_list = list(map(int, puzzle_input.read().split("\n")))

preamble_length = 25

def preamble(input_list, preamble_length):
    sums = {}
    last_x = collections.deque(input_list[:preamble_length])
    for x, y in itertools.combinations(input_list[:preamble_length], 2):
        if x+y in sums:
            sums[x+y].extend([x, y])
        else:
            sums[x+y] = [x, y]
    return sums, last_x


def remove_old_sums(comparison_dict, comparison_deque, number):
    for member in comparison_deque:
        total = member + number
        if len(comparison_dict[total]) == 2:
            del comparison_dict[total]
        else:
            comparison_dict[total].remove(member)
            comparison_dict[total].remove(number)


def add_new_nums(comparison_dict, comparison_deque, number):
    for member in comparison_deque:
        total = member + number
        if total in comparison_dict:
            comparison_dict[total].extend([member, number])
        else:
            comparison_dict[total] = [member, number]


def solve_one(input_list):
    comparison_dict, comparison_deque = preamble(input_list, preamble_length)
    for number in input_list[preamble_length:]:
        if number not in comparison_dict:
            return number
        else:
            element_to_remove = comparison_deque.popleft()
            remove_old_sums(comparison_dict, comparison_deque, element_to_remove)
            comparison_deque.append(number)
            add_new_nums(comparison_dict, comparison_deque, number)



print(solve_one(input_list))