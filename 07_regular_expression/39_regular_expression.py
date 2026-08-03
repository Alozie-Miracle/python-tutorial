import re

# splitting a string by comma
text = "one,two,three,four,five,six,seven,eight,nine,ten"

fileds = re.split(r",", text) # split the string by comma
# print(f"Fields: {fileds}")

# you can do more than splitting on commas, youcan split on new line
text2 = "one, two, three, four, five, six, seven, eight, nine, ten"
fields2 = re.split(r"\s*,\s*", text2) # split the string by new line
# print(f"Fields2: {fields2}") 

# replacing a string using regex
text = "Hello Jack, How are you doing today? Jack is a good boy"

text = re.sub(r"Jack", "Jill", text) # replace Jack with Jill


# alternatively
text = re.sub(r"J\w+", "Jill", text) # replace Jack with Jill
# print(f"Replaced Text: {text}")

text = text.replace("Jack", "Jill") # replace Jack with Jill

text = "Hello Jack, Hello Zoe, Hello Sam"
# alternative to regex
# text = re.sub(r"Jack|Zoe|Sam", "???", text) #-> Hello ???, Hello ???, Hello ???

text = re.sub(r"Hello (Jack|Zoe|Sam)", r"Hi \1", text) #-> Hi Jack, Hi Zoe, Hi Sam
# print(text)




# Ignoring cases in regex
text = "Hello Bob"

# print(re.search(r"hello", text, re.IGNORECASE)) #-> <re.Match object; span=(0, 5), match='Hello'>


# print(re.search(r".*bob", text, re.IGNORECASE)) #-> <re.Match object; span=(0, 9), match='Hello Bob'>


# print(re.sub(r"bob", "Zoe", text, flags=re.IGNORECASE)) #-> Hello Zoe


# COMPILING REGULAR EXPRESSIONS
text = "Oranges are my favorite fruit. I like to eat oranges every day."

# print(re.sub(r"O\w+s", "Apples", text)) #-> Apples are my favorite fruit. I like to eat Apples every day.


regex = re.compile(r"O\w+s", re.IGNORECASE) # compile the regex pattern


# print(re.sub(regex, "Apples", text))




# Zero-width lookhead assertions

text = "You could get a developer job. E.g. in robotics. Maybe. Or web developement."

result = re.findall(r"\s+(\w+)\.\s?", text)
print(result) # ['job', 'robotics', 'developement']

result = re.findall(r"\s+(\w+)\.(?=\s+|$)", text)
print(result) # ['job', 'robotics', 'Maybe', 'developement']
