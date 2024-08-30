s = s = "cbbd"

#recursion solution
memo={}
def dp(l,r):

    
    if l<0 or r>len(s)-1:
        return 0
    if s[l]==s[r]:
        return dp(l-1,r+1)+2
    if (l,r) in memo:
        return memo[(l,r)]
    else:
        memo[(l,r)]=max(dp(l-1,r),dp(l,r+1))
        return max(dp(l-1,r),dp(l,r+1))
    
mx=1    
for i in range(len(s)):
    if mx<dp(i-1,i+1)+1:
        mx=dp(i-1,i+1)+1

for j in range(0,len(s)-2):
    if s[j]==s[j+1]:
        if mx<dp(j-1,(j+1)+1)+2:
           mx=dp(j-1,(j+1)+1)+2
print(mx)           