
def int_x(string):
    if string == "x":
        return None
    else:
        return int(string)

with open("day_13.txt", 'r') as puzzle_input:
    input = puzzle_input.read().split("\n")
    #input = [0, "67,7,59,61"]
bus_numbers = input[1].split(",")
buses = list()
remainders = {}
for index, entry in enumerate(bus_numbers):
    if int_x(entry):
        buses.append(int_x(entry))
        remainders[int_x(entry)] = index % int_x(entry)

"""
find smallest x s.t.
x = 0 mod 37
x = 27 mod 41
x = 37 mod 457
...
"""
M = 1
for x in buses:
    M *= x

ms = {}
for x in buses:
    ms[x] = M//x

invs = {}
for x in buses:
    to_invert = ms[x] % x
    for y in range(x):
        if (y * to_invert) % x == 1:
            invs[x] = y
            break

for x in buses:
    print(f"{x}, remainder = {remainders[x]}, Mx = {ms[x]}, Mx mod x = {ms[x] % x}, multiplied by inverse is {((ms[x] % x) * invs[x]) % x} inverse = {invs[x]}")


answer = 0
for x in buses:
    answer += remainders[x] * ms[x] * invs[x]
print(answer)

for x in buses:
    print(answer % x)
print((M - answer) % M)
print(M)