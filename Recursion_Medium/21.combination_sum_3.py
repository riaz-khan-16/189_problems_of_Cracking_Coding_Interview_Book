candidates = [1,2,3,4,5,6,7,8,9]
target = 9
k=3
# candidates =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# target=27
# candidates.sort()
ans=[]

def combination(p,sum, index,target,arr,k):

    if len(p)>k:
        return

    if len(p)==k:
        if sum==target :
           ans.append(p[0:])
           return 
        if sum>target:
           return
        

    for i in range(index, len(arr)):
        if i>index and arr[i]==arr[i-1]:
            continue

        p.append(arr[i])
        sum=sum+arr[i]
        combination(p,sum, i+1,target,arr,k)
        p.pop()
        sum=sum-arr[i]

combination([],0,0,target,candidates,k)        


   
     
print(ans)