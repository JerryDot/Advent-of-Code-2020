
with open("day_one.txt", 'r') as puzzle_input:
    expense_list = [int(line) for line in puzzle_input]

search_set = set()

for price in expense_list:
    if price in search_set:
        print(f"Answer is {price} and {2020-price}")
        print(f"Multiplied these give {price * (2020-price)}")
    else:
        search_set.add(2020-price)
