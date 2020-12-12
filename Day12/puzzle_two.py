
with open("day_twelve.txt", 'r') as puzzle_input:
    text_input = puzzle_input.read().split("\n")
    commands = [[line[0], int(line[1:])] for line in text_input]


class Ship:
    def __init__(self):
        # the following two refer to the waypoint
        self.east = 10
        self.north = 1

        self.travel_east = 0
        self.travel_north = 0


def rotate(ship, direction_turning, degrees):
    for x in range(int(degrees/90)):
        if direction_turning == "L":
            ship.east, ship.north = -ship.north, ship.east
        else:
            ship.east, ship.north = ship.north, -ship.east


def translate_ship(ship, heading, value):
    if heading == "N":
        ship.north += value
    elif heading == "S":
        ship.north -= value
    elif heading == "E":
        ship.east += value
    elif heading == "W":
        ship.east -= value


def forward(ship, value):
    ship.travel_east += ship.east * value
    ship.travel_north += ship.north * value


translations = set(["W", "E", "N", "S"])
rotations = set(["R", "L"])


new_ship = Ship()
for line in commands:
    if line[0] in translations:
        translate_ship(new_ship, line[0], line[1])
    elif line[0] in rotations:
        rotate(new_ship, line[0], line[1])
    else:
        forward(new_ship, line[1])

print(abs(new_ship.travel_east) + abs(new_ship.travel_north))
