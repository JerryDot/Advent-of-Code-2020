
with open("day_eighteen.txt", 'r') as puzzle_input:
    input_sums = puzzle_input.read().split("\n")


def resolve_brackets(arithmetic):
    if "(" not in arithmetic:
        return sums(arithmetic)
    else:
        starting_bracket = arithmetic.index("(")
        brackets_to_resolve = 1
        search_index = starting_bracket
        while brackets_to_resolve > 0:
            search_index += 1
            if arithmetic[search_index] == "(":
                brackets_to_resolve += 1
            elif arithmetic[search_index] == ")":
                brackets_to_resolve -= 1
        ending_bracket = search_index
        new_string = arithmetic[:starting_bracket] + str(resolve_brackets(arithmetic[starting_bracket + 1:ending_bracket])) \
                     + arithmetic[ending_bracket+1:]
        return resolve_brackets(new_string)


def int_plus(stuff):
    if stuff.isnumeric():
        return int(stuff)
    else:
        return stuff


def sums(arithmetic):
    things = list(map(int_plus, arithmetic.split(" ")))
    while "+" in things:
        plus_location = things.index("+")
        things[plus_location] = things[plus_location - 1] + things[plus_location + 1]
        del things[plus_location+1]
        del things[plus_location-1]

    calculation = things[0]
    operations_indices = [i for i in range(len(things)) if i % 2 == 1]
    for index in operations_indices:
        calculation *= things[index + 1]
    return calculation


total = 0
for question in input_sums:
    total += resolve_brackets(question)
print(total)
