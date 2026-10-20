s = input()
words = s.split()
minlen = len(words[0])
for w in words:
    if len(w) < minlen:
        minlen = len(w)
print(minlen)
