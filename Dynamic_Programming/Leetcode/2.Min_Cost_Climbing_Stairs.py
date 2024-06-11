cost = [1,100,1,1,1]
cost = [10,15,20]

#recursive method

def f(cost,p,c):
    if p+1==len(cost) or p+2==len(cost):
        
        return c
    return min(f(cost,p+1,c+cost[p+1]),f(cost,p+2,c+cost[p+2]))


#Dymanic Programming Memoization
x=[-1]*len(cost)
def f(n):
    if  n<2:
        x[n]=cost[n]
        return x[n]
    if x[n]!=-1:
        return x[n]
    if x[n]==-1:
        x[n]=cost[n]+min(f(n-1),f(n-2))
        return x[n]

n=len(cost)
print(min(f(n-1),f(n-2)))

#Dynamic Programming  Tabular approach

memo=[0]*n
def dp(n):
    memo[0]=cost[0]
    memo[1]=cost[1]
    for i in range(2,n):
        memo[i]=cost[i]+min(memo[i-1],memo[i-2])

dp(n)
print(min(memo[n-1],memo[n-2]))











    


