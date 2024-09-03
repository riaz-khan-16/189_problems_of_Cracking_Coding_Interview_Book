#https://leetcode.com/problems/pascals-triangle/description/



def pascal(last):
    new=[1]
    for i in range(len(last)-1):
        new.append(last[i]+last[i+1])
    new.append(1)
    return new
first=[1]
second=[1,1]
n=5
ans=[]
for i in range(n):
    if i==0:
        ans.append(first)
    elif i==1:
        ans.append(second)
    else:
        ans.append(pascal(ans[-1]))
print(ans)


