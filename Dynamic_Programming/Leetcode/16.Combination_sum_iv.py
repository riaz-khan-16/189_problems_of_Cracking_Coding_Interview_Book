arr=[1,2,3]
target=4
memo=[-1]*(target+1)
def f(x):
    if x==0:
        return 1
    if x<0:
        return 0
    
    if memo[x] != -1:
        return memo[x]
    else:
        res=0
        for i in arr:
            res=res+f(x-i)
        memo[x]=res
        return  memo[x]
  
ans=0
for k in arr:
    ans=ans+f(target-k)
print(ans)    