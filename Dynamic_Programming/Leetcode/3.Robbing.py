#Leetcode 198

arr=[2,7,9,3,1]

arr = [1,2,3,1]
arr =[2,1,1,2]
#recursive solution

def f(i):

    if i>=len(arr):
        return 0
    #take current house
    left=arr[i]+f(i+2)
    right=f(i+1)

    return max(left,right)


#Memoization 

mem=[-1]*len(arr)

def dp(i,mem):

    if i>=len(arr):
        return 0
    if mem[i]!=-1:
        return mem[i]
    if mem[i]==-1:
        mem[i]=max(arr[i]+dp(i+2,mem),dp(i+1,mem))
        return mem[i]
    



# Tabular method
memo=[0]*len(arr)
def dpt(memo):
    memo[0]=arr[0]
    memo[1]=max(arr[0],arr[1])
    for i in range(1,len(arr)):
        memo[i]=max(arr[i]+memo[i-2],memo[i-1])
        
dpt(memo)
print(memo[len(arr)-1])

#
