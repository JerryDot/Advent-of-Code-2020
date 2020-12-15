"""
mask = 00010010001010101XXXX000000X111X0111
mem[32507] = 5127835
mem[25226] = 65531297
mem[41033] = 582
mask = 001X10X011XX10001110X10X0010101X1X1X
mem[43059] = 28874
mem[43129] = 672
mem[270] = 121337
mem[14460] = 800244
mem[49574] = 1609
"""

with open("day_fourteen.txt", 'r') as puzzle_input:
    raw_input = puzzle_input.read().split("mask = ")
    del raw_input[0]
    print(raw_input)
    less_raw_input = [x.split("\nmem[") for x in raw_input]
    print(less_raw_input)
    even_less_raw_input = {}
    for entry in less_raw_input:
        even_less_raw_input[entry[0]] = []
        for allocation in entry[1:]:
            even_less_raw_input[entry[0]].append(allocation.split("] = "))
    print(even_less_raw_input)


def int_to_bin36(integer):
    string = format(integer, 'b')
    corrected_string = "0" * (36 - len(string)) + string
    return corrected_string


def apply_mask(mask, bin_36):
    output = ""
    for index, character in enumerate(mask):
        if character == "X":
            output += bin_36[index]
        else:
            output += character
    return output


def bin36_to_int(bin_36):
    return int(bin_36, 2)


memory = {}
for collection in even_less_raw_input:
    bitmask = collection
    for memory_alloc in even_less_raw_input[collection]:
        memory_location = int(memory_alloc[0])
        value = int(memory_alloc[1])
        memory[memory_location] = bin36_to_int(apply_mask(bitmask, int_to_bin36(value)))

print(memory)
sum = 0
for entry in memory:
    sum += memory[entry]
print(sum)


