#last weight stone
stone=[31,26,33,21,40]
memo={}
def dp(i,w):
    if i==len(stone):
        return abs(w)
    if (i,w) in memo:
        return memo[i,w]
    else:
        plus=dp(i+1,w+stone[i])
        minus=dp(i+1,w-stone[i])
        memo[(i,w)]=min(plus,minus)
        return min(plus,minus)
    
res=dp(0,0)

print(res)
