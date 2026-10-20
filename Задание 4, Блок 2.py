s = input()
words = s.split()
cnt = 0
for w in words:
    if w.count('А') == 3:
        cnt += 1
print(cnt)
