s = input()
words = s.split()
maxlen = 0
for w in words:
    if len(w) > maxlen:
        maxlen = len(w)
print(maxlen)
