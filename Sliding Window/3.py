#https://leetcode.com/problems/longest-repeating-character-replacement/description/
from collections import Counter
s = "ABABBA"
k = 1

count={}
res=0

l=0
for r in range(len(s)):
    count[s[r]]=1+count.get(s[r],0)
    while (r-l+1)-max(count.values())>k:
        count[s[l]]=-1
        l=l+1
    
    res=max(res,(r-l+1))
print(res)





