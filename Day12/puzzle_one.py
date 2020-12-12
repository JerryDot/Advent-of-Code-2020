
with open("day_twelve.txt", 'r') as puzzle_input:
    text_input = puzzle_input.read().split("\n")
    commands = [[line[0], int(line[1:])] for line in text_input]


class Ship:
    def __init__(self):
        self.east = 0
        self.north = 0
        self.direction = "E"


direction_map = {0: "E", 1: "S", 2: "W", 3:"N",
                 "E": 0, "S": 1, "W": 2, "N": 3}


def rotate(ship, direction_turning, degrees):
    if direction_turning == "R":
        ship.direction = direction_map[(direction_map[ship.direction] + degrees/90) % 4]
    elif direction_turning == "L":
        ship.direction = direction_map[(direction_map[ship.direction] - degrees/90) % 4]


def translate_ship(ship, heading, value):
    if heading == "N":
        ship.north += value
    elif heading == "S":
        ship.north -= value
    elif heading == "E":
        ship.east += value
    elif heading == "W":
        ship.east -= value


def forward(ship, direction_facing, value):
    translate_ship(ship, direction_facing, value)


translations = set(["W", "E", "N", "S"])
rotations = set(["R", "L"])

new_ship = Ship()
for line in commands:
    if line[0] in translations:
        translate_ship(new_ship, line[0], line[1])
    elif line[0] in rotations:
        rotate(new_ship, line[0], line[1])
    else:
        forward(new_ship, new_ship.direction, line[1])
print(abs(new_ship.east) + abs(new_ship.north))
