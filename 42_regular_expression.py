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
print(text)

