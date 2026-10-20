s = input()
res = ''
for c in s:
    if 'A' <= c <= 'Z':
        res += c.lower()
    else:
        res += c
print(res)
