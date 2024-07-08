#https://leetcode.com/problems/decode-ways/description/

#recursive solution


s='226' #it is the given string
memo={}
def rec(ans,i):
    if i in memo:
        return memo[i]
    if i>=len(s):
        return 1
    if s[i]=='0':
        return 0
    x=rec(ans+[s[i]],i+1)

    if i<len(s)-1 and int(s[i]+s[i+1])<=26 and int(s[i])>0:
      x=x+rec(ans+[s[i]+s[i+1]],i+2)

    memo[i]=x   
    return x  
print(rec([],0))





