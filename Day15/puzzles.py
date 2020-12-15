import copy

starting_numbers = [0, 1, 5, 10, 3, 12, 19]


def nth_number(starting_numbers, n):
    numbers = copy.deepcopy(starting_numbers)
    numbers_last = dict()
    for index, value in enumerate(starting_numbers[:-1]):
        numbers_last[value] = index
    x = len(numbers) - 1

    while x < n - 1:
        if numbers[-1] not in numbers_last:
            numbers_last[numbers[-1]] = x
            numbers.append(0)
        else:
            distance = x - numbers_last[numbers[-1]]
            numbers_last[numbers[-1]] = x
            numbers.append(distance)
        x += 1
    return numbers[-1]


print(nth_number(starting_numbers, 2020))
print(nth_number(starting_numbers, 30000000))