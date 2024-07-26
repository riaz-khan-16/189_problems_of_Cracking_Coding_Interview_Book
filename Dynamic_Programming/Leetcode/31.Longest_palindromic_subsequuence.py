s = s = "cbbd"


def dp(l,r,t):
    if l<0 or r>len(s)-1:
        return t
    if s[l]==s[r]:
        return dp(l-1,r+1,t+2)
    else:
        return max(dp(l-1,r,t),dp(l,r+1,t))
    
mx=1    
for i in range(len(s)):
    if mx<dp(i-1,i+1,1):
        mx=dp(i-1,i+1,1)

for j in range(0,len(s)-2):
    if s[j]==s[j+1]:
        if mx<dp(j-1,(j+1)+1,2):
           mx=dp(j-1,(j+1)+1,2)