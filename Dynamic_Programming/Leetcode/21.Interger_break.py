n=6
memo={}
def dp(p,up,last):
    
 
    if up==0 and last!=n:
        return p
    if (p,up) in memo:
        return memo[(p,up)]
    mx=0
    for i in range(1,up+1):

        mx=max(dp(p*i,up-i,i),mx)

    memo[(p,up)]=mx
    return  mx
mx=dp(1,n,0)

print(mx)