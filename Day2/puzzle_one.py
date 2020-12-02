# example line: "3-14 v: vvpvvvmvvvvvvvv"

with open("day_two.txt", 'r') as puzzle_input:
    no_valid = 0
    for line in puzzle_input:
        terms = line.split(" ")
        terms[0] = terms[0].split("-")
        letter_to_search = terms[1][0]
        count = 0
        for letter in terms[2][:-1]:
            if letter == letter_to_search:
                count += 1
        if int(terms[0][0]) <= count <= int(terms[0][1]):
            no_valid += 1
    print(no_valid)


