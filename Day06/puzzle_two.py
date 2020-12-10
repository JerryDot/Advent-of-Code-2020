
with open("day_six.txt", 'r') as puzzle_input:
    group_responses = puzzle_input.read().split("\n\n")

count = 0
for submission in group_responses:
    individual_responses = submission.split("\n")
    number_of_people = len(individual_responses)
    common_answers = set(individual_responses[0])

    for x in range(number_of_people - 1):
        new_answers = set(individual_responses[x + 1])
        common_answers = common_answers.intersection(new_answers)
    count += len(common_answers)

print(count)
