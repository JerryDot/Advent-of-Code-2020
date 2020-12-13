
def int_x(string):
    if string == "x":
        return 0
    else:
        return int(string)

with open("day_13.txt", 'r') as puzzle_input:
    input = puzzle_input.read().split("\n")
    waiting_time = int(input[0])
    buses = list(map(int_x, input[1].split(",")))


print(input)
print(buses)

times_to_wait = {}
soonest_bus = 1000
queueing_time = 1000
for bus in buses:
    print(soonest_bus)
    print(queueing_time)
    if bus != 0:
        times_to_wait[bus] = bus - (waiting_time % bus)
        print(f"bus is {bus} and its time is {times_to_wait}")
        if times_to_wait[bus] < queueing_time:
            queueing_time = times_to_wait[bus]
            soonest_bus = bus

print(soonest_bus)
print(queueing_time)
print(waiting_time % bus)
print(soonest_bus * queueing_time)
