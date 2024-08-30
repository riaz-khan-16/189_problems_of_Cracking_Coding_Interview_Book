# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

s = "abcabcbb"
l=0
charset=set()
res=0
for r in range(len(s)):
    while s[r] in charset:
        charset.remove(s[l])
        l=l+1
    charset.add(s[r])
    res=max(res,r-l+1)
print(res)
    
