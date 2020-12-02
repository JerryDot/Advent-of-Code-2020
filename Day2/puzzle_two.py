# example line: "3-14 v: vvpvvvmvvvvvvvv"

with open("day_two.txt", 'r') as puzzle_input:
    no_valid = 0
    for line in puzzle_input:
        terms = line.split(" ")
        terms[0] = terms[0].split("-")
        first_position = int(terms[0][0])
        second_position = int(terms[0][1])
        letter_to_search = terms[1][0]
        if (letter_to_search == terms[2][first_position-1]) ^ \
                (letter_to_search == terms[2][second_position-1]):
            no_valid += 1
    print(no_valid)