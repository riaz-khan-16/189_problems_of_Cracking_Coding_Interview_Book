arr =[1,2,3,4]



#recursive solution
def f(i,arr):

    if i>=len(arr):
        return 0
    #take current house
    left=arr[i]+f(i+2,arr)
    right=f(i+1,arr)

    return max(left,right)

n=len(arr)
res=max(f(0,arr[:-1]), f(0,arr[1:]))


#Dynamic Programming memoization
arr =[1,2,3,1]
mem=[-1]*len(arr)

def dp(i,mem,arr):

    if i>=len(arr):
        return 0
    if mem[i]!=-1:
        return mem[i]
    if mem[i]==-1:
        mem[i]=max(arr[i]+dp(i+2,mem,arr),dp(i+1,mem,arr))
        return mem[i]
mem=[-1]*len(arr)
res1=(dp(0,mem,arr[:-1]))   
mem=[-1]*len(arr)
res2=(dp(0,mem,arr[1:]))
print(max(res1,res2)) 



    

