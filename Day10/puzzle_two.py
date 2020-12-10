from itertools import chain, combinations

with open("day_ten.txt", 'r') as puzzle_input:
    input_list = list(map(int, puzzle_input.read().split("\n")))

input_list.sort()
input_list.insert(0, 0)
input_list.insert(0, -3)
input_list.append(input_list[-1] + 3)
print(input_list)


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


possible_counts = dict()

def count_possible(x):
    if x in possible_counts:
        return possible_counts[x]
    print(x)
    count = 0
    for selection in powerset(range(1, x)):
        list_to_check = [0]
        list_to_check.extend(list(selection))
        list_to_check.append(x)
        print(list_to_check)
        if check_possible(list_to_check):
            count += 1
    possible_counts[x] = count
    return count


def check_possible(adapter_list):
    for first, second in zip(adapter_list, adapter_list[1:]):
        if second - first > 3:
            return False
    return True


total = 1
counter = 0
for first, second in zip(input_list, input_list[1:]):
    if second - first == 1:
        counter += 1
    elif second - first == 3:
        total *= count_possible(counter)
        counter = 0
print(total)

print(possible_counts)