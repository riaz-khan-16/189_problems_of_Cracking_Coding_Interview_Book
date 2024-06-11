arr=[2,3,7,8,10]
sum=10

#Recursion Approach
def f(p,up,s):
    if not up:
        return False
    if s==sum:
        
        return True
        
    return f(p+[up[0]],up[1:],s+up[0]) or f(p,up[1:],s)
    
    
    

print(f([],arr,0))

