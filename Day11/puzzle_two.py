from operator import add

with open("day_eleven.txt", 'r') as puzzle_input:
    seat_map = list(map(list, puzzle_input.read().split("\n")))

y_size = len(seat_map)
x_size = len(seat_map[0])

print(seat_map)


def seat_in_bounds(seat):
    x = seat[0]
    y = seat[1]
    if x in range(x_size) and y in range(y_size):
        return True
    else:
        return False



to_check = {}

def check_direction(position, direction, array):
    seat_to_check = list(map(add, position, list(direction)))
    if seat_in_bounds(seat_to_check):
        if array[seat_to_check[1]][seat_to_check[0]] == ".":
            return check_direction(seat_to_check, direction, array)
        elif array[seat_to_check[1]][seat_to_check[0]] == "#":
            return "#"
        else:
            return "L"
    else:
        return "."



def determine_next(x, y, old_array):
    count = dict()
    count["#"] = 0
    count["L"] = 0
    count["."] = 0
    directions_to_check = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
    for direction in directions_to_check:
        count[check_direction([x, y], direction, old_array)] += 1

    if old_array[y][x] == "L" and count["#"] == 0:
        return "#"
    elif old_array[y][x] == "#" and count["#"] >= 5:
        return "L"
    else:
        return old_array[y][x]


def update(array):
    return_array = []
    for y in range(y_size):
        row = []
        for x in range(x_size):
            row.append(determine_next(x, y, array))
        return_array.append(row)
    return return_array


def count(array, symbol):
    count = 0
    for row in array:
        for column in row:
            if column == symbol:
                count += 1
    return count


starting_array = seat_map

while True:
    updated_array = update(starting_array)
    if updated_array == starting_array:
        print(count(updated_array, "#"))
        break
    starting_array = updated_array
