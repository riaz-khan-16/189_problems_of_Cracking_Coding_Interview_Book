coins = [1, 2, 5]
amount = 11




#Dynamic Programming


def f(coins,amount):

    dp=[amount+1]*(amount+1) 
    dp[0]=0

    for i in range(amount+1):
        for k in coins:
               if i-k>=0:
                    dp[i]=min(dp[i],1+dp[i-k])

    return dp[amount]                
                    
print(f(coins,amount))