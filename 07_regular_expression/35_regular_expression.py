# to compaire strength
# note if yue use "r" in front of "" then you don't need \\
# \\w matches alphanumeric characters
# \\w* or \w+ matches all preceeding characters
# \\s matches space
# .* matches everything
# *? matches as little as possible
# *?$ matches as mucha s possible
# \\d matches digits
# \\d+ matches digits as many digits as possible
# \\.
# \w{2,40} matches range from 2 to 4
# \- and \. matches hiphens and dot

import re

text = "dog"

result = re.match("dog", text)


# to check if a text starts with "d" and ends with "t"
result = re.match("d.g", text)
# print(result is not None)


result = re.match("dd.g", text)
# print(result is not None)


# matching mutlple characters
text = "drooooooooool"
result = re.match("dro*l", text) #the o* matches as many as o'es are there

# alternatively
result = re.match("dr*", text) #the * matches everything


# if result is None:
#     print("no match")
# else:
#     print(result.group())


# ternary operator
value = 7
text = "Condition is true" if value < 3 else "Condition is false"
# print(text)



# greedy and not greedy matching
text = "zigzag"

result = re.match("z.*g", text)
# print("No match" if result is None else f"Match: {result.group()}" )


result = re.match("z.*?g", text)
# print("No match" if result is None else f"Match: {result.group()}" )


result = re.match("z.*?", text)
# print("No match" if result is None else f"Match: {result.group()}" )

result = re.match("z.*?$", text)
# print("No match" if result is None else f"Match: {result.group()}" )



# matching words and numbers using regular expression
# \w: matches alphanumeric characters
text = "The temperature is 37."
result = re.match("\\w", text)  # matches T
# print("No match" if result is None else f"Match: {result.group()}" )


result = re.match("\\w\\w\\w", text) #matches The

# print("No match" if result is None else f"Match: {result.group()}" )

# note \w doesn't match space

result = re.match("\\w*", text) #matches The

# print("No match" if result is None else f"Match: {result.group()}" )

# /w+ matches one or more, as many as possible
result = re.match("\\w+", text) #matches The

# print("No match" if result is None else f"Match: {result.group()}" )

# to match a space we use \\s
result = re.match("\\w+\\s\\w+", text) #matches The

# print("No match" if result is None else f"Match: {result.group()}" )

# to match digits
result = re.match("\\w+\\s\\w+\\s\\w+\\s\\d+", text) #matches The

# print("No match" if result is None else f"Match: {result.group()}" )

# to match a dot
result = re.match("\\w+\\s\\w+\\s\\w+\\s\\d+\\.", text) #matches The

# print("No match" if result is None else f"Match: {result.group()}" )

text = "The price is 400"
result = re.match("\\w+\\s\\w+\\s\\w+\\s\\d+", text) #matches The

# print("No match" if result is None else f"Match: {result.group()}" )


text = "The temperature is: 37"
result = re.match(".*:\\s*\\d+", text) #matches The

# print("No match" if result is None else f"Match: {result.group()}" )

# capture groups
result = re.match(r".*:\s*(\d+)", text) #everything

# print("No match" if result is None else f"Match: {result.group(1)}" ) # prints 37



# matching specific numbers of characters
email = "john@caveofprogramming.com"

result = re.match(r"\w{2,30}@\w{2,40}\.\w{2,10}", email) #{4} or {2,4} is a range

# print("No match" if result is None else f"Match: {result.group()}" )


# character matching
text = 'abc'

result = re.match(r"[abc]", text) #matches a
# print(result.group())

# using [a-z]
result = re.match(r"[a-z]+", text) #matches abc
# print(result.group())


# to match either a-z or digits
result = re.match(r"[a-z/d]+", text) #matches a to z or digits
# print(result.group())

# \- and \. matches hiphens and dot
result = re.match(r"[a-z/d\-\.\d]+", "ab.-.c34") #matches a to z and digits
print(result.group())
