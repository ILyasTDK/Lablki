s = input()

has_vowel = any(c.lower() in "aeiou" for c in s)

print("Yes" if has_vowel else "No")