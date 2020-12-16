
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


def is_ticket_valid(ticket):
    if any(number in invalid for number in ticket):
        return False
    else:
        return True


valid_tickets = []
valid_tickets.append(your_ticket)
for ticket in nearby_tickets:
    if is_ticket_valid(ticket):
        valid_tickets.append(ticket)
print(len(valid_tickets))

print(your_ticket)
print(nearby_tickets)
print(field_list)

for entry in field_list:
    valid_indexes = []
    for index in range(len(valid_tickets[0])):
        if all(number_in_field(number, entry) for number in [row[index] for row in valid_tickets]):
            valid_indexes.append(index)
    print(f"valid indices for {entry} are {valid_indexes}")

print(your_ticket[3])
print(your_ticket[4])
print(your_ticket[12])
print(your_ticket[14])
print(your_ticket[15])
print(your_ticket[17])
print(179*157*227*199*223*181)
