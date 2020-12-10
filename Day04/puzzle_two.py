import re
from termcolor import colored

with open("day_four.txt", 'r') as puzzle_input:
    id_cards = puzzle_input.read().split("\n\n")

data_list = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
color_match = re.compile(r"#[0-9a-f]{6}")
eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def invalid(field, entry):
    if field == "byr":
        if not 1920 <= int(entry) <= 2002:
            return True

    if field == "iyr":
        if not 2010 <= int(entry) <= 2020:
            return True

    if field == "eyr":
        if not 2020 <= int(entry) <= 2030:
            return True

    if field == "hgt":
        if entry[-2:] == "cm":
            if not 150 <= int(entry.strip("cm")) <= 193:
                return True
        elif entry[-2:] == "in":
            if not 59 <= int(entry.strip("in")) <= 76:
                return True
        else:
            return True

    if field == "hcl":
        if not color_match.match(entry):
            return True

    if field == "ecl":
        if entry not in eye_colors:
            return True

    if field == "pid":
        if len(entry) != 9:
            return True
        if not entry.isnumeric():
            return True
    return False


def check_validity(credentials):
    if all(data in credentials for data in data_list):
        for data in credentials:
            if invalid(data, credentials[data]):
                return False
        return True


count = 0
for person in id_cards:
    to_check = {}
    stats_list = re.split("\n| ", person)
    for entry in stats_list:
        new_data = entry.split(":")
        to_check[new_data[0]] = new_data[1]

    if check_validity(to_check):
        count += 1

print(count)