A='bd'
B='abcd'
memo={}

def dp(i,j):
    
    if i>len(A)-1 or j>len(B)-1:
        return 0
    if (i,j) in memo:
        return memo[(i,j)]
    
    elif A[i]==B[j]:
        memo[(i,j)]=1+dp(i+1,j+1)
        return 1+dp(i+1,j+1)
    
    else:
        memo[(i,j)]=max(dp(i+1,j),dp(i,j+1))
        return max(dp(i+1,j),dp(i,j+1))

print(dp(0,0))