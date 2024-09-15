#https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7



potions.sort()
def checkSuccess(s):
    l=0
    r=len(potions)-1
    while l<=r:
        mid=(l+r)//2
        if potions[mid]*s<success:
            l=mid+1
        else:
            r=mid-1
    return l

    

for i in range(len(spells)):
    spells[i]=len(potions)-checkSuccess(spells[i])
print(spells)
