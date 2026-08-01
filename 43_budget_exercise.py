import re

expenditure = """
Day        Electricity   Coffee      Cleaning     Wifi
Monday     330           10          50           20
Tuesday    220           12          40           25
Wednesday  120           14          80           30
Thursday   150           16          60           35
"""


# TODO
# write out how much is spent everyday
# how much on electricity total
# how much on coffee total
# how much on cleaning total


results = re.findall(r"(\w+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", expenditure)
# print(results)

total_spent_aday = []

for result in results:
    day = 0
    for i, data in enumerate(result):
        if i > 0:
            day += int(data)
    total_spent_aday.append(day)

for i, result in enumerate(results):
    print(f"Total spent on {result[0]}: {total_spent_aday[i]}")
print()

bills_names = re.findall(r"(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)", expenditure)[0][1:]  # get the first match which contains the category names
list_of_bills = list(bills_names) 


total_amounts = [0 for x in range(len(results[0])-1)]  # create a list of zeros with the same length as the number of categories
for i, result in enumerate(results):
    for j, value in enumerate(result):
        if j > 0:  # Skip the day name
            total_amounts[j-1] += int(value) # converts the string to int and adds to the total
    
for i, bill in enumerate(list_of_bills):
    print(f"Total spent on {bill}: {total_amounts[i]}")
print()


total_spent = sum(total_amounts)
print(f"Total spent: {total_spent}")

