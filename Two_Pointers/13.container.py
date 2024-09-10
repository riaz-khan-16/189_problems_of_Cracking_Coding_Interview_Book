#https://leetcode.com/problems/container-with-most-water/description/

height = [1,8,6,2,5,4,8,3,7]

left=0
right=len(height)-1

minarea=0
while left<right:
    area=min(height[left],height[right])* (right-left)
    if area>minarea:
        minarea=area
    if height[left]<height[right]:
        left=left+1
    else:
        right=right-1
print(minarea)