# 97. Interleaving String

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

memo={}
def dp(i,j,k):

    if i==len(s1) and j==len(s2) and k==len(s3):
        return True
    
    if (i,j,k) in memo:
        return memo[(i,j,k)]

    if i<len(s1) and s1[i]==s3[k]:
        if dp(i+1,j,k+1):
            memo[(i,j,k)]=True

            return True
    if j<len(s2) and s2[j]==s3[k]:
        if dp(i,j+1,k+1):
            memo[(i,j,k)]=True
            return True
    

    return False
    

print(dp(0,0,0))
