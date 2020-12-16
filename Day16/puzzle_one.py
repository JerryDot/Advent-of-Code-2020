"""
departure location: 41-526 or 547-973
departure station: 29-874 or 891-961
departure platform: 25-200 or 213-966
departure track: 38-131 or 152-951
departure date: 29-349 or 366-955
departure time: 34-450 or 464-958
arrival location: 28-635 or 650-962
arrival station: 25-663 or 689-955
arrival platform: 49-731 or 738-955
arrival track: 50-617 or 627-970
class: 39-90 or 98-966
duration: 32-99 or 120-949
price: 43-742 or 756-955
route: 32-501 or 520-968
row: 41-276 or 285-951
seat: 30-830 or 840-972
train: 31-123 or 131-974
type: 35-63 or 75-949
wagon: 26-564 or 580-951
zone: 47-380 or 402-952

your ticket:
197,173,229,179,157,83,89,79,193,53,163,59,227,131,199,223,61,181,167,191

nearby tickets:
153,109,923,689,426,793,483,628,843,774,785,841,63,168,314,725,489,339,231,914
177,714,226,83,177,199,186,227,474,942,978,440,905,346,788,700,346,247,925,825
98,718,599,348,225,261,310,490,773,867,659,874,286,290,408,481,780,240,309,391
549,157,51,253,338,559,185,820,914,412,180,88,811,426,420,715,557,325,9,700
"""

with open("day_sixteen.txt", 'r') as r:
    puzzle_input = r.read().split("\n\n")

fields = puzzle_input[0].split("\n")
your_ticket = list(map(int, puzzle_input[1][13:].split(",")))
nearby_tickets = puzzle_input[2][16:].split("\n")
nearby_tickets = [list(map(int, x.split(","))) for x in nearby_tickets]

field_list = []
for field in fields:
    first_split = field.split(": ")
    second_split = first_split[1].split(" or ")
    numbers = [list(map(int, second_split[0].split("-"))), list(map(int, second_split[1].split("-")))]
    field_list.append(numbers)


def number_in_field(number, field):
    if field[0][0] <= number <= field[0][1] or field[1][0] <= number <= field[1][1]:
        return True


valid = set()
invalid = set()
for number in range(1000):
    if number in valid or number in invalid:
        pass
    else:
        if any(number_in_field(number, field) for field in field_list):
            valid.add(number)
        else:
            invalid.add(number)


def ticket_validity(ticket):
    count = 0
    for number in ticket:
        if number in invalid:
            count += number
    return count


count_invalid = 0
for ticket in nearby_tickets:
    count_invalid += ticket_validity(ticket)

print(count_invalid)


print(your_ticket)
print(nearby_tickets)
print(fields)

