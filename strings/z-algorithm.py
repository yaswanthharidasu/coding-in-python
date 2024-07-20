s = [1, 0, 1, -1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0]
Z = [0]*len(s)

l = r = 0
for i in range(1, len(s)):
    if i > r:
        l = r = i
        while r < len(s) and s[r-l] == s[r]:
            r += 1
        r -= 1
        Z[i] = r-l+1
    else:
        k = i-l
        if i+Z[k] < r:
            Z[i] = Z[k]
        else:
            l = i
            while r < len(s) and s[r-l] == s[r]:
                r += 1
            r -= 1
            Z[i] = r-l+1

print(Z)