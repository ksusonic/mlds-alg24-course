s = input()

p = [0] * len(s)
d = [0] * len(s)

for i in range(1, len(s)):
    j = p[i - 1]
    while j > 0 and s[i] != s[j]:
        j = p[j - 1]

    d[i] = d[j]
    if s[i] == s[j]:
        d[i] += 1
        j += 1

    p[i] = j

max_prefix_i = max(range(len(d)), key=d.__getitem__) - d[0] + 1
print(s[:max_prefix_i])
