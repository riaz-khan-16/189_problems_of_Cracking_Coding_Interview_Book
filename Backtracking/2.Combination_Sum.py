
# https://leetcode.com/problems/combination-sum/description/

arr=[2,3,5,7]
ans=[]
def combination(arr,csum,ccomb,cindex,target,ans):
    
       if csum>target:
           return 
       if csum==target:
           ans.append(ccomb[0:])
           print(ccomb)
           return 
       for i in range(cindex, len(arr)):
           ccomb.append(arr[i])
           csum=csum+arr[i]
           combination(arr,csum,ccomb,i,target,ans)
           ccomb.pop()
           csum=csum-arr[i]
           
           


    
ccom=[]    
combination(arr,0,ccom,0,7,ans) 
print(ans)   


           



