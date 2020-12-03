import itertools

with open("day_one.txt", 'r') as puzzle_input:
    expense_list = [int(line) for line in puzzle_input]

for a, b, c in itertools.combinations(expense_list, 3):
    if a + b + c == 2020:
        print(f"answers are {a}, {b} and {c}")
        print(f"multiplying gives {a * b * c}")
