
expense_list = []
with open("day_one.txt", 'r') as puzzle_input:
    for line in puzzle_input:
        expense_list.append(int(line))

first_pass = set(expense_list)
second_pass = dict()

for cost in expense_list:
    for price in first_pass:
        second_pass[cost+price] = [cost, price]

for cost in expense_list:
    for sum in second_pass:
        if cost + sum == 2020:
            print(f"answers are {cost}, {second_pass[sum][0]} and {second_pass[sum][1]}")
            print(f"multiplying gives {cost*second_pass[sum][0]*second_pass[sum][1]}")
