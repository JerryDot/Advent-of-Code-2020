
with open("day_eight.txt", 'r') as puzzle_input:
    raw_instructions = puzzle_input.read().split("\n")


def parse_instruction(string):
    to_return = string.split(" ")
    to_return[1] = int(to_return[1])
    to_return.append(False)
    return to_return


def run_code(instruction_list):
    accumulator = 0
    head = 0
    # This section is revamped into a better form in the answer to the second question
    while instruction_list[head][2] is False:
        instruction_list[head][2] = True
        if instruction_list[head][0] == "acc":
            accumulator += instruction_list[head][1]
            head += 1
        elif instruction_list[head][0] == "nop":
            head += 1
        else:
            head += instruction_list[head][1]
    return accumulator


clean_instructions = [parse_instruction(line) for line in raw_instructions]
print(run_code(clean_instructions))
