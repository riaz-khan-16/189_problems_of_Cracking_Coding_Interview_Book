#https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/

nums = [2,3,3,4,6,7] 
target = 12
MOD = 10**9 + 7
nums.sort()
left=0
right=len(nums)-1
res=0
while left<=right:
    if nums[left]+nums[right]<=target:
        res=res+2**(right-left)
        res=res%MOD
        left=left+1
    else:
        right=right-1
    
print(res)
