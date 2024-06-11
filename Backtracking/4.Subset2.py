
ans=[]
def f(p,up):
    
    if not up:
        ans.append(p[0:])
        return 
    p.append(up[0])
    f(p,up[1:])

    p.pop()
    while len(up)>1 and up[0]==up[1]:
        up=up[1:]
    f(p,up[1:])


f([],[1,1,2,2]) 
print(ans)