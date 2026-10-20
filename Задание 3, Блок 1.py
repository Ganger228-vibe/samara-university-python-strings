s = input()
cnt = 0
for c in s:
    if 'a' <= c <= 'z' or 'а' <= c <= 'я' or c == 'ё':
        cnt += 1
print(cnt)
