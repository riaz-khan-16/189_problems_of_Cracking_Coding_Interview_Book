arr=[2,3,6,7]

l=[]
def f(x,p,up):
    global l
    if p>7:
        return
    elif p==7:
        l.append(x)
        print(x)
        return 
    for i in up:
        f(x+[i],p+i,up)
f([],0,arr)  
for i in l:
    i.sort()

x=[]
for i in (l):
    if i not in x:
        x.append(i)




print(x)



