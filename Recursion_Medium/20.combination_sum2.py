candidates = [10,1,2,7,6,1,5]
target = 8
# candidates =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# target=27
candidates.sort()
ans=[]

def combination(p,sum, index,target,arr):

    if sum==target:
        ans.append(p[0:])
        return 
    if sum>target:
        return
    for i in range(index, len(arr)):
        if i>index and arr[i]==arr[i-1]:
            continue

        p.append(arr[i])
        sum=sum+arr[i]
        combination(p,sum, i+1,target,arr)
        p.pop()
        sum=sum-arr[i]

combination([],0,0,target,candidates)        


   
     
print(ans)

      
  