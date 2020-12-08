import re

with open("day_seven.txt", 'r') as puzzle_input:
    bag_text = puzzle_input.read().split("\n")

bag_rules = {}


def parse_bag(string, puzzle_no):
    if puzzle_no == 1:
        if string[0].isnumeric():
            return string[2:-5]
        else:
            return None
    if puzzle_no == 2:
        if string[0].isnumeric():
            return string[2:-5], int(string[0])
        else:
            return None


for rule in bag_text:
    rule_to_parse = rule.replace("bag,", "bags,")
    rule_to_parse = rule_to_parse.replace("bag.", "bags")
    rule_to_parse = rule_to_parse.replace("bags.", "bags")
    rule_to_parse = re.split(" contain |, ", rule_to_parse)
    bag_rules[rule_to_parse[0][:-5]] = [parse_bag(rule, 2) for rule in rule_to_parse[1:]]
    print(rule_to_parse)

print(bag_rules)
"""
def search_for_gold(bag, base_level=0):
    if "shiny gold" in bag_rules[bag]:
        return True
    else:
        for other_bag in bag_rules[bag]:
            if other_bag is None:
                pass
            else:
                if search_for_gold(other_bag, 1):
                    return True
    if base_level == 0:
        return False
"""

def count_bags(base_bag, number_of_base_bags=1):
    count = 0
    for bag_no in bag_rules[base_bag]:
        if bag_no is None:
            pass
        else:
            count += bag_no[1] * number_of_base_bags
            count += count_bags(bag_no[0], bag_no[1]) * number_of_base_bags
    return count

def solve_two(bag_rules):
    print(count_bags("shiny gold"))

solve_two(bag_rules)
