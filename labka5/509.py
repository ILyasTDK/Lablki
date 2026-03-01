import re

s = input()

matches = re.findall(r'\b\w{3}\b', s)
print(len(matches))