# 63. Unique Paths II

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,1],[0,0]]
m=len(obstacleGrid)-1
n=len(obstacleGrid[0])-1
def dp(m,n):
    if m==1 and n==1:
        return 1
    if m<0 or n<0:
        return 0
    if obstacleGrid[m][n]==1:
        return 0
    return dp(m,n-1)+dp(m-1,n)
print(dp(m,n))