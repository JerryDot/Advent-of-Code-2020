import copy

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
        if character == "0":
            output += bin_36[index]
        else:
            output += character
    return output


bin_strings = {0: [], 1: ["0", "1"]}
def binary_strings(n):
    if n in bin_strings:
        return bin_strings[n]
    strings = list()
    for word in binary_strings(n-1):
        strings.append("0" + word)
        strings.append("1" + word)
    return strings


def calculate_addresses(masked):
    addresses = []
    substitutions = binary_strings(masked.count("X"))
    if len(substitutions) == 0:
        return masked

    for sub in substitutions:
        index = 0
        word = ""
        for character in masked:
            if character != "X":
                word += character
            else:
                word += sub[index]
                index += 1
        addresses.append(word)

    return addresses


def bin36_to_int(bin_36):
    return int(bin_36, 2)


memory = {}
for collection in even_less_raw_input:
    bitmask = collection
    for memory_alloc in even_less_raw_input[bitmask]:
        memory_location = int_to_bin36(int(memory_alloc[0]))
        value = int(memory_alloc[1])
        masked_memory = apply_mask(bitmask, memory_location)
        for address in calculate_addresses(masked_memory):
            memory[bin36_to_int(address)] = value

print(memory)
sum = 0
for entry in memory:
    sum += memory[entry]
print(sum)
