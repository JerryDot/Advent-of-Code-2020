
with open("day_five.txt", 'r') as puzzle_input:
    boarding_passes = puzzle_input.read().split("\n")


def binary_to_int(one_c, zero_c, string):
    x = string.replace(one_c, "1").replace(zero_c, "0")
    return int(x, 2)


seat_ids = [binary_to_int("B", "F", b_pass[:7]) * 8 +
            binary_to_int("R", "L", b_pass[7:]) for b_pass in boarding_passes]

print(max(seat_ids))

