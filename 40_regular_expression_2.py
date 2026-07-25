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

print(id, content)