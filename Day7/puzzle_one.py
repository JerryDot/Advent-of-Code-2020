import re

# O(n)
with open("day_seven.txt", 'r') as puzzle_input:
    bag_text = puzzle_input.read().split("\n")

bag_rules = {}

# O(1)
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

# O(n)
for rule in bag_text:
    rule_to_parse = rule.replace("bag,", "bags,")
    rule_to_parse = rule_to_parse.replace("bag.", "bags")
    rule_to_parse = rule_to_parse.replace("bags.", "bags")
    rule_to_parse = re.split(" contain |, ", rule_to_parse)
    bag_rules[rule_to_parse[0][:-5]] = [parse_bag(rule, 1) for rule in rule_to_parse[1:]]
    print(rule_to_parse)

search_results = {}
def search_for_gold(bag):
    if bag in search_results:
        return search_results[bag]

    if "shiny gold" in bag_rules[bag]:
        search_results[bag] = True
        return True
    else:
        for other_bag in bag_rules[bag]:
            if other_bag is None:
                pass
            else:
                if search_for_gold(other_bag):
                    search_results[bag] = True
                    return True
    search_results[bag] = False

# do search for gold n times
def solve_one(bag_rules):
    count = 0
    for bag in bag_rules:
        if search_for_gold(bag):
            count += 1
    print(count)


solve_one(bag_rules)
