#maximum-alternating-subsequence-sum


nums = [4,2,5,3]

memo={}
def rec(i,next):
    if i==len(nums):
       return 0
    if (i,next) in memo:
       return memo[(i,next)]
    if next=='Odd':
      include=-nums[i]+rec(i+1,'Even')
      exclude=rec(i+1,'Odd')
    else:
      include=nums[i]+rec(i+1,'Odd')
      exclude=rec(i+1,'Even')
    memo[(i,next)]=max(include,exclude)  
    return max(include,exclude)     

print(rec(0,'Even') )  