arr=[1,2,3]

def f(arr):
        outer=[]
        outer.append([])
        for i in arr: 
            n=len(outer)
            for k in range(n):
                x=outer[k]
                internal=x.copy()
                internal.append(i)
                outer.append(internal)
        return outer
ans=f(arr)
print(ans) 


