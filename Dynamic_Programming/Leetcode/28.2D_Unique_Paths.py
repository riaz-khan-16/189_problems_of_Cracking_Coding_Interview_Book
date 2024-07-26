

m=3
n=7

hash={}
def dp(m,n):
    if m==1 and n==1:
        return 1
    if m<0 or n<0:
        return 0
    if (m,n) in hash:
        return hash[(m,n)]
    hash[(m,n)]=dp(m,n-1)+dp(m-1,n)
    return dp(m,n-1)+dp(m-1,n)
    
def dp_tbl(m,n):
        dp = [[1]*n for i in range(m)]
        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]



                            