def build(s):
    lsp = [0]*len(s)
    for i in range(1, len(s)):
        j = lsp[i-1]
        while j > 0 and s[i] != s[j]:
            j = lsp[j-1]
        if s[i] == s[j]:
            j += 1
        lsp[i] = j
    return lsp

s = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]
p = [0, 1, 1, 0, 1]

lsp = build(p)
ans = list()
j = 0

for i in range(len(s)):
    while j > 0 and s[i] != p[j]:
        j = lsp[j-1]
    if s[i] == p[j]:
        j += 1
    if j == len(p):
        ans.append(i-j+1)
        j = lsp[j-1]
        
print(ans) 
