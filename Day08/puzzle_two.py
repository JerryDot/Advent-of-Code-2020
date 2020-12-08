import copy
with open("day_eight.txt", 'r') as puzzle_input:
    raw_instructions = puzzle_input.read().split("\n")


def parse_instruction(string):
    to_return = string.split(" ")
    to_return[1] = int(to_return[1])
    return to_return


def jmp_nop_switch(instruction_list, switch_index):
    if instruction_list[switch_index][0] == "jmp":
        instruction_list[switch_index][0] = "nop"
    elif instruction_list[switch_index][0] == "nop":
        instruction_list[switch_index][0] = "jmp"


def run_code(instruction_list):
    accumulator = 0
    head = 0
    previously_seen = set()

    while head != len(instruction_list):
        if head not in previously_seen:
            previously_seen.add(head)
            if instruction_list[head][0] == "acc":
                accumulator += instruction_list[head][1]
                head += 1
            elif instruction_list[head][0] == "nop":
                head += 1
            else:
                head += instruction_list[head][1]
        else:
            break

    if head == len(instruction_list):
        return accumulator


clean_instructions = [parse_instruction(line) for line in raw_instructions]
for index in range(len(clean_instructions)):
    jmp_nop_switch(clean_instructions, index)
    x = run_code(clean_instructions)
    jmp_nop_switch(clean_instructions, index)
    if x:
        print(x)
        break

