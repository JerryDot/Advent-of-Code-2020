
with open("day_nineteen.txt", 'r') as puzzle_input:
    input_split = puzzle_input.read().split("\n\n")
    rules = input_split[0].split("\n")
    messages = input_split[1].split("\n")

for rule in rules:
    split_rule = rule.split(":")

