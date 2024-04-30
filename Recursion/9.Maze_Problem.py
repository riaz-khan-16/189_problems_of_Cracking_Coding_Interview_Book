def f(p,r,c):
    if r==1 and c==1:
        l=[]
        l.append(p)
        print(p)
        return l

    x=[]
    if c>1:
        x=x+(f(p+'R',r,c-1))

    if r>1:
       x=x+f(p+'D',r-1,c)
    if c>1 and r>1:
        x=x+f(p+'Dia',r-1,c-1)

    return x  
 
def f1(p,r,c):
    if r==1 and c==1:
        print(p)
        return 
    if r==2 and c==2:

        return 
   
    if c>1:
        (f1(p+'R',r,c-1))
    if r>1:
       f1(p+'D',r-1,c)
     
    
f1('',3,3)