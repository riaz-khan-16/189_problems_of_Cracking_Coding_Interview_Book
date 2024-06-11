n=3


#Normal Recursive Way

def findSteps(n):
   
    if n<0:
        return 0
    if n==0:
        return 1
    
    left=findSteps(n-1)

    right=findSteps(n-2)

    return left+right

#Dynamic Programming Memoization
memo=[-1]*(n+1)

def findStepsDP(n,memo):
    if n<0:
        return 0
    if n==0:
        return 1
    if memo[n]!=-1:
        return  memo[n]
    if memo[n]==-1:
        memo[n]=findStepsDP(n-1,memo)+findStepsDP(n-2,memo)
        return memo[n]


#Dynamic Programming Bottom Up approach
n=3

def findStepsDPTabular(n,memo):
    memo=[0]*(n+1) 
    memo[0]=1
    memo[1]=1
    for i in range(2,n+1):
        memo[i]=memo[i-1]+memo[i-2]
    print(memo[n])
    return memo[n]    

findStepsDPTabular(n,memo)
   








