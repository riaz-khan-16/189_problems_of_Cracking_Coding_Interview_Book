
res=[]
def f(p,up):

    if p and p[-1]!=p[-1][::-1]:
        return

    if not up:
        res.append(p[0:])
        return

    for i in range(len(up)):
        f(p+[up[0:i+1]],up[i+1:])
    



   


          
    
       

f([],'efe')
# f('','bc',[])
# f('','c',[])
print(res)
    
  