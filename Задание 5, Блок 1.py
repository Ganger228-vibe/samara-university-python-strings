s = input()
res = ''
for c in s:
    if 'a' <= c <= 'z' or 'а' <= c <= 'я' or c == 'ё':
        res += c.upper()
    else:
        res += c
print(res)
