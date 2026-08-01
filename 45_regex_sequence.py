import re

text = r"""
    Canada[a] is a country in North America. Its ten provinces and three territories extend from the Atlantic Ocean to the Pacific Ocean and northward into the Arctic Ocean, 
making it the second-largest country by total area, with the longest coastline of any country. Its border with the United States is the longest international land border. 
The country is characterized by a wide range of both meteorologic and geological regions. With a population of over 41 million, it has widely varying population densities, 
with the majority residing in its urban areas and large areas being sparsely populated. Its capital is Ottawa and its three largest metropolitan areas are Toronto, Montreal, and Vancouver.

Indigenous peoples have continuously inhabited what is now Canada for thousands of years. Beginning in the 16th century, British and French expeditions explored and later settled along the Atlantic coast. 
As a consequence of various armed conflicts, France ceded nearly all of its colonies in North America in 1763. In 1867, with the union of three British North American colonies through Confederation, 
Canada was formed as a federal dominion of four provinces. This began an accretion of provinces and territories resulting in the displacement of Indigenous populations, and a process of increasing autonomy 
from the United Kingdom. This increased sovereignty was highlighted by the Statute of Westminster, 1931, and culminated in the Canada Act 1982, which severed the vestiges of legal dependence on the 
Parliament of the United Kingdom.
"""



# NOTE
# \S: not space = [^\s]
# \W: not alphanumeric = [^\w]
# \D: not digit = [^\d]


not_space = set(re.findall(r"\S", text)) # find all non-space characters
print(f"Not Space: {not_space}")
print()
not_alphanumeric = set(re.findall(r"\W", text)) # find all non-alphanumeric characters
print(f"Not Alphanumeric: {not_alphanumeric}")


# Summary
# . wildcard character
# \s whitespace character
# \S not whitespace character
# \w alphanumeric character
# \W not alphanumeric character
# \d digit character
# \D not digit character
# \r\f carriage return and form feed characters
# \r\n newline character

# [] character class
# () grouping
# (?: ) non-capturing group
# (?=) positive lookahead
# (?!) negative lookahead
# | alternation

# re.I ignore case
# re.M multi-line
# re.DOTALL dot matches all characters including newline

# search() returns a match object if there is a match anywhere in the string
# findall() returns a list of all matches in the string
# sub() replaces all matches in the string with a specified string
# split() splits the string at each match and returns a list of substrings
# compile() compiles a regex pattern into a regex object for reuse
# match() checks for a match only at the beginning of the string
# fullmatch() checks for a match only if the entire string matches the pattern

# * zero or more occurrences
# ? zero or one occurrence
# *? zero or more occurrences, non-greedy
# + one or more occurrences
# +? one or more occurrences, non-greedy
