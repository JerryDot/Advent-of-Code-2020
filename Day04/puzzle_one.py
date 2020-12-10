import re
from termcolor import colored

with open("day_four.txt", 'r') as puzzle_input:
    id_cards = puzzle_input.read().split("\n\n")

data_list = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def check_validity(credentials):
    if all(data in credentials for data in data_list):
        return True


count = 0
for person in id_cards:
    to_check = {}
    print(person)
    stats_list = re.split("\n| ", person)
    print(stats_list)
    for entry in stats_list:
        new_data = entry.split(":")
        to_check[new_data[0]] = new_data[1]

    print(to_check)
    print(colored(len(to_check), "red"))
    if check_validity(to_check):
        print("True!")
        count += 1
    else:
        print(colored("False!", "cyan"))
print(count)



print(id_cards)
