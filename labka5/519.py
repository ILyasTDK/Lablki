import re

s = input()

pattern = re.compile(r'\b\w+\b')

matches = pattern.findall(s)
print(len(matches))