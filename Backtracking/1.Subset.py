#https://leetcode.com/problems/subsets/description/

res=[]
def f(p,up):
    
    if not up:
        res.append(p.copy())
        return 
    p.append(up[0])
    f(p,up[1:])

    p.pop()
    f(p,up[1:])
   
f([],[1,2,2])  
print(res)  