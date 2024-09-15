#https://leetcode.com/problems/find-peak-element/description/


nums = [1,2,1,3,5,6,4]


l=0
r=len(nums)-1
while l<=r:
    m=(l+r)//2
    if m>0 and nums[m]<nums[m-1]:
        r=m-1
    elif m<len(nums) and nums[m]<nums[m+1]:
        l=m+1
    else:
        print(m)
        break

