nums = [9,4,1,7,5]
k = 3
nums.sort()

left=0
right=k-1
minimum=float("inf")

while left<len(nums) and right<len(nums):
    diff=nums[right]-nums[left]
    if diff <minimum:
        minimum=diff
    left=left+1
    right=right+1
print(minimum)

