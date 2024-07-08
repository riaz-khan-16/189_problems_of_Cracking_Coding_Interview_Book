s = "leetcode"
wordDict = ["leet","code"]

# s = "applepenapple"
# wordDict = ["apple","pen"]

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]


s="cars"
wordDict =["car","ca","rs"]

def rec(p):
    if len(p)>len(s):
        return False
    
    if p==s:
        return True
    for word in wordDict:
        if rec(p+word):
            return True
    return False

def dp(s):
    dp=[False]*(len(s)+1)
    dp[len(s)]=True
    for i in range(len(s)-1,-1,-1):
        for w in wordDict:
           if i+len(w)<=len(s) and s[i:i+len(w)]==w:
               dp[i]=dp[i+len(w)]
             

    return dp[0]         
                 
x=dp(s)
print(x)                   
               