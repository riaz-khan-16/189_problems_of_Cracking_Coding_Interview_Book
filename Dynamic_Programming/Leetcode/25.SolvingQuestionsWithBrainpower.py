#Solving Questions With Brainpower

questions = [[3,2],[4,3],[4,4],[2,5]]
questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]


memo={}
def dp(i):

    if i>len(questions)-1:
        return 0
    
    if i in memo:
        return memo[i]
    else:
        memo[i]=max(questions[i][0]+dp(i+questions[i][1]+1),dp(i+1))
    return max(questions[i][0]+dp(i+questions[i][1]+1),dp(i+1))

print(dp(0))