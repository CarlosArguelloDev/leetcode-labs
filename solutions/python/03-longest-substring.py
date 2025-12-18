s = "pwwkew"
chars = set()
left = 0
long = 0

for right in range (len(s)):
    while s[right] in chars:
        chars.remove(s[left])
        left += 1
    chars.add(s[right])
    long = max(long, right - left + 1)
    

print(long)