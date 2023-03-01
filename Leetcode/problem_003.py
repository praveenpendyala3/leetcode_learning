s = "aa"
        
l = 0
r = 1

ss_len = 0
while l<len(s) and r<len(s):
    print(l, r, s[r], s[l:r])
    if s[r] in s[l:r]:
        if r-l > ss_len:
            ss_len = r-l
        l = s[l:r].index(s[r]) + 1 + l
        r = l + 1
        continue
    
    if r == len(s)-1:
        if r-l+1 > ss_len:
            ss_len = r-l+1
            break
    
    r = r + 1

if ss_len == 0:
    ss_len = len(s)

print(ss_len)