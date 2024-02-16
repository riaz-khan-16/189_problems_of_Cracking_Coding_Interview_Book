
arr=[5,5,1,2,2]
k=3
s=set(arr)
m={}
for i in arr:
    m[i]=arr.count(i)
sorted_n=sorted(m.values()) 
u=len(s)
for x in sorted_n:
   if k>=x:
       k=k-x
       u=u-1
   else:
       break
print(u)         

