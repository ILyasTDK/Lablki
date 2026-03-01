import re

s = input()

pattern = r"Name: (.+), Age: (.+)"
match = re.match(pattern, s)

if match:
    name, age = match.groups()
    print(name, age)