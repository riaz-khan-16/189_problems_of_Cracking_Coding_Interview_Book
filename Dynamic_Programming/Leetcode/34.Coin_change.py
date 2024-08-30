# coing change

amount = 5
coins = [1,2,5]
memo={}
def dp(total,i):
    if total==5:
        return 1
    if total>5 or i>=len(coins):
        return 0
    if (total,i) in memo:
        return memo[(total,i)]
    else:
        memo[(total,i)]=dp(total+coins[i],i)+dp(total,i+1)
   
        return memo[(total,i)]
    

  
res=dp(0,0)  
print(res)
