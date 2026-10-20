s = input()
words = s.split()
cnt = 0
for w in words:
    if w[0] == w[-1]:
        cnt += 1
print(cnt)
