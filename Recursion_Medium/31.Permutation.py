s='abcd'

#add a character in all possible position of a string

def addeverypoint(x,s):
    y=[]
    for i in range(len(s)+1):
        y.append(s[0:i]+x+s[i:])
    return y    


def dp(res,s):
    if not s:
        return res
    
    if not res:
        res.append(s[0])
        return dp(res,s[1:])
    
    else:
        y=[]
        for i in res:
            y=y+addeverypoint(s[0],i)
            
        res=[]
        res=res+y
        return dp(res,s[1:])
print(dp([],s))








          
