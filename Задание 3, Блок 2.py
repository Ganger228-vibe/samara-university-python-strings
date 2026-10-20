s = input()
words = s.split()
cnt = 0
for w in words:
    if 'А' in w:
        cnt += 1
print(cnt)
