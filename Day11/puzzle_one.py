
with open("day_eleven.txt", 'r') as puzzle_input:
    seat_map = list(map(list, puzzle_input.read().split("\n")))

y_dim = len(seat_map)
x_dim = len(seat_map[0])

print(seat_map)


def determine_next(x, y, old_array):
    count = dict()
    count["#"] = 0
    count["L"] = 0
    count["."] = 0
    points_to_check = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    for point in points_to_check:
        if 0 <= point[0] < x_dim and 0 <= point[1] < y_dim:
            if old_array[point[1]][point[0]] in count:
                count[old_array[point[1]][point[0]]] += 1
            else:
                count[old_array[point[1]][point[0]]] = 1

    if old_array[y][x] == "L" and count["#"] == 0:
        return "#"
    elif old_array[y][x] == "#" and count["#"] >= 4:
        return "L"
    else:
        return old_array[y][x]


def update(array):
    return_array = []
    for y in range(y_dim):
        row = []
        for x in range(x_dim):
            row.append(determine_next(x, y, array))
        return_array.append(row)
    return return_array


def count(array, symbol):
    counter = 0
    for row in array:
        for column in row:
            if column == symbol:
                counter += 1
    return counter


starting_array = seat_map

while True:
    updated_array = update(starting_array)
    if updated_array == starting_array:
        print(count(updated_array, "#"))
        break
    starting_array = updated_array
