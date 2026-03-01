import re

s=input()

result=re.findall(r"\d",s)
print(" ".join(result))