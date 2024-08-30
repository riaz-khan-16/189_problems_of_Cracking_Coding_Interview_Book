# 309. Best Time to Buy and Sell Stock with Cooldown


prices = [1,2,3,0,2]
prices =[1,2,4]

def dp(i,last_state):
    if i>=len(prices):
        return 0

    if last_state:
        return max(prices[i]+dp(i+2,False),dp(i+1,True))
        
    else:
        return max(dp(i+1,False),-prices[i]+dp(i+1,True))
    

res=dp(0,False)  
