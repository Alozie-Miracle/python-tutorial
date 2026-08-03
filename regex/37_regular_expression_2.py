import re

# using not character class
# ^> shows that > give you all the things that's not > and stops at >.
# < -> gives <
# [^>]+ -> gives everything that comes before >
# > -> gives you >
# [^<>]+ -> gives you everything that's not <>
# <[^>]+ -> gives you everthing from < and stops before >
#> gives you the last >

tag = "<div id='123'>Hello</div>"

result = re.match(r"<[^>]+>[^<>]+<[^>]+>", tag)

# print(result.group())


# escpaing regexes
text = "-\n-"
# print(text)

text = r"-\n-"
# print(text)

# print(re.match(r"-\\n-", text)) #give the result




# comment and space in regular expression
tag = "<div id='123'>Hello</div>"

result = re.match(
    r"""
        <div\s+    # Match opening tag
        id='(\w+)'   # Match Id attribute
        >          # Match of opening tag
        ([^<>]+)    # Match content of tag
        </div>     # Closing div tag

    """, 
    tag, re.VERBOSE)

id, content = result.groups()


result = re.match(
    r"""
        <(\w+)\s+    # Match opening tag
        id='(\w+)'   # Match Id attribute
        >          # Match of opening tag
        ([^<>]+)    # Match content of tag
        </\1>     # Gives the first opening tag

    """, 
    tag, re.VERBOSE)

# if result is None:
#     print("No Match")
# else:
#     tag, id, content = result.groups()

#     print(tag, id, content)


# Capturing groups and non groups

email = "one.two.three.four@example.com"

result = re.match(r'(\w+\.)(\w+\.)', email)
# print(result.group(0)) #prints everything
# print(result.group(1)) # print the first 

result = re.match(r'(\w+\.)*', email)
# print(result.group(0)) #prints everything that ends with a dot

result = re.match(r'(\w+\.)*\w+\@\w+\.\w+', email)
# print(result.group(0)) #prints everything

# to print capture groups
result = re.match(r'(?:\w+\.)*\w+\@\w+\.\w+', email)
# print(result.groups()) #gives ()

result = re.match(r'((?:\w+\.)*)\w+\@\w+\.\w+', email)
# print(result.groups()) #gives ('one.two.three.',)




# matching newlines
text = """
    one
    two
    three
"""

# print(re.match(r"one", text)) #returns none
# print(re.match(r"\s*one\s*two", text)) #matches the space and '\n    one\n    two'

# alternatievly
# print(re.match(r".*one", text, re.DOTALL)) #give one -> <re.Match object; span=(0, 8), match='\n    one'>
# print(re.match(r".*two", text, re.DOTALL)) #give one -> <re.Match object; span=(0, 16), match='\n    one\n    two'>


#matching ends of lines
result = re.match(r"(.*two)", text, re.DOTALL) 


# if result is None:
#     print("No match")
# else:
#     print(f"Match: '{result.group(1)}'")
"""
Match: '
    one
    two'
"""

    
result = re.match(r"(.*?two)", text, re.DOTALL)

# if result is None:
#     print("No match")
# else:
#     print(f"Match: '{result.group(1)}'")

"""
Match: '
    one
    two'
"""

# to match the end of the string
result = re.match(r"(.*?two.*?)$", text, re.DOTALL)

# if result is None:
#     print("No match")
# else:
#     print(f"Match: '{result.group(1)}'") #matches everything


# result = re.match(r"(.*?two.*?)$", text, re.DOTALL | re.MULTILINE)
# if result is None:
#     print("No match")
# else:
#     print(f"Match: '{result.group(1)}'") #non greedy match, matches end of the line and not the end of the string, does not match three


# using search function
text = """
    one
    two
    three
    four
    five
"""


result = re.search(r"two", text) # matches two
# if result is None:
#     print("No match")
# else:
#     print(f"Match: '{result.group(0)}'") 


result = re.search(r"t.*e", text) # matches three
# if result is None:
#     print("No match")
# else:
#     print(f"Match: '{result.group(0)}'") 


result = re.search(r"t.*e", text, re.DOTALL) # matches everything starting with t and the end of the string
# if result is None:
#     print("No match")
# else:
#     print(f"Match: '{result.group(0)}'") 



# using find all function
text = """
1. Apple
2. Orange
3. Cherries
4. Strawberries
"""


result = re.findall(r"\d\.\s\w+", text) #returns ['1. Apple', '2. Orange', '3. Cherries', '4. Strawberries']
# result = re.findall(r"(\d\.\s\w+)", text) # alternative

# print(result)

# to separate the number and the words
result = re.findall(r"(\d\.)\s(\w+)", text) # gives a list of tupple -> [('1.', 'Apple'), ('2.', 'Orange'), ('3.', 'Cherries'), ('4.', 'Strawberri
# print(result)
