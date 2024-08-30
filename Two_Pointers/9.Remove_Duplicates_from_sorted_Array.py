# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

nums = [1,1,1,2,2,3]
l=0
j=0


while j<len(nums) :
    count=1
    while j+1<len(nums) and nums[j]==nums[j+1]:
        count=count+1
        j=j+1
    for i in range(min(2,count)):
        nums[l]=nums[j]
        l=l+1
    j=j+1


print(l)



    


       
  
