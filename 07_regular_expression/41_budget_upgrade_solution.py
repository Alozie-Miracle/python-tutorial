import re
from collections import defaultdict

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


lines = re.split("\n", expenditure)
header = None
category = defaultdict(float)  # create a dictionary to hold the total amounts for each category
days = defaultdict(float)  # create a dictionary to hold the total amounts for each day

for line in lines:
    if re.search(r"^\s*$", line):
        continue  # skip empty lines

    fields = re.split(r"\s+", line)
    if header is None:
        header = fields  # first non-empty line is the header
        continue
    
    day = fields.pop(0) # remove the first field which is the day name

    for i, field in enumerate(fields):
        days[day] += float(field)  # add the value to the total for the day

        heading = header[i+1]  # get the corresponding heading for the field
        category[heading] += float(field)  # add the value to the total for the

    


    
print(header)
print(days)
print(category)