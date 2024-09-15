#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
nums=[4,5,6,7,0,1,2]
l,r=0,len(nums)-1
if nums[0]<nums[-1]:
    ans=nums[0]
if nums[-2]>nums[-1]<nums[0]:
    ans=ans[-1]

while l<=r:
    m=(l+r)//2
    if (m-1>=0 and m+1<len(nums)) and nums[m-1]>nums[m]<nums[m+1]:
        ans=nums[m]
        break
    elif nums[m]>nums[r]:
        l=m+1
    elif nums[m]<nums[l]:
        r=m-1
print(ans)