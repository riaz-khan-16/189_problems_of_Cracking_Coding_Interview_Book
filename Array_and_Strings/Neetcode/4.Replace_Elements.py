# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/


arr = [17,18,5,4,6,1]

rightmax=-1
for i in range(len(arr)-1,-1,-1):
    newmax=max(rightmax, arr[i])
    arr[i]=rightmax
    rightmax=newmax
print(arr)




