#https://leetcode.com/problems/rotate-array/description/

nums = [1,2,3,4,5,6,7]
k = 3

for i in range(k+1):
    x=nums.pop()
    nums.append(x)
print(nums)

