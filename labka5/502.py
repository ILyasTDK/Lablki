import re

s = input()
t = input()

if re.search(t, s):
    print("Yes")
else:
    print("No")