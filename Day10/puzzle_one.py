
with open("day_ten.txt", 'r') as puzzle_input:
    input_list = list(map(int, puzzle_input.read().split("\n")))

input_list.sort()
count = [0, 0, 0]

count[input_list[0] - 1] += 1
count[2] += 1

for first, second in zip(input_list, input_list[1:]):
    count[second - first - 1] += 1

print(count[0] * count[2])

