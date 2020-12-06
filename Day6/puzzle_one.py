
with open("day_six.txt", 'r') as puzzle_input:
    answers = puzzle_input.read().split("\n\n")

count = 0
for answer in answers:
    x = answer.replace("\n", "")
    set_x = set(x)
    count += len(set_x)
print(count)
