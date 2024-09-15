#https://leetcode.com/problems/search-a-2d-matrix/description/

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

#at first find the row
def findRow(matrix):
        l=0
        r=len(matrix)-1
        while l<=r:
            m=(l+r)//2
            if matrix[m][0]>target and matrix[m][-1]>target:
                r=m-1
            elif matrix[m][0]<target and matrix[m][-1]<target:
                l=l+1
            elif matrix[m][0]<=target and matrix[m][-1]>=target:
                return m
        return -1
m=findRow(matrix)
print(m)

def findCol(m,matrix):
    l=0
    r=len(matrix[0])-1
    while l<=r:
        me=(l+r)//2
        if matrix[m][me]==target:
            return True
        elif matrix[m][me]>target:
            r=r-1
        elif matrix[m][me]<target:
            l=l+1
    return False
if m!=-1:
    print(findCol(m,matrix))
else:
    print(False)

    
