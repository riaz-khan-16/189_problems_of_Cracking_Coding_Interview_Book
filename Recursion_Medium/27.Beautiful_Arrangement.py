n=15
arr=[]

for i in range(n):
    arr.append(i+1)

ans=0
def f(p,up):
    global ans
    if len(p)==len(arr):
        ans=ans+1
        
        return 

    for i in range(len(up)):

        if (i+1)%up[i]==0 or up[i]%(i+1)==0:    
            f(p+[up[i]],(up[0:i]+up[i+1:])) 


f([], arr)        
print(ans)