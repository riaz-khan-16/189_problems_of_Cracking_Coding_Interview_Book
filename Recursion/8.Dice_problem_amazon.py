

def dice(p,up):
    if up==0:
        l=[]
        l.append(p)
        print(p)
        return l
    li=[] 
    for i in range(1,up+1):
        li=li+dice(p+str(i),up-i)
    return li

x=dice('',4)    
print(x)       