# https://leetcode.com/problems/find-pivot-index/description/

nums = [1]
nums = [1,2,3]
nums = [2,1,-1]


sum=0
for i in nums:
    sum=sum+i

left=0
right=sum-nums[0]
if left==right:
    print(0)

for i in range(1,len(nums)):
    left=left+nums[i-1]
    right=right-nums[i]
    if left==right:
        print(i)

