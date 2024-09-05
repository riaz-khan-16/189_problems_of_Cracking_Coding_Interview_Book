# https://leetcode.com/problems/move-zeroes/description/

nums=[0,1,0,3,12]

for i in range(len(nums)-1,-1,-1):
    if nums[i]==0:
        #swape until next element is last index or zero
        while i+1<len(nums) and nums[i+1]!=0:
            nums[i],nums[i+1]=nums[i+1],nums[i]
            i=i+1
print(nums)
