# fint the regular expression for john.purcell@caveprogramming.com

import re

# result = re.match("[a-z/.@]+", "john.purcell@caveprogramming.com")
result = re.match(r"([a-z][a-z\.\-]+)@(\w+).(\w+)", "john.purcell@caveprogramming.com")

name, domain, suffix = result.groups()

print(name, domain, suffix)