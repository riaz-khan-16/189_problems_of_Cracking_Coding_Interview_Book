# N = 3
# P = 2
# S = 23 
N = 4
P = 3
S = 54

def isPrime(x):
    y=x**(1/2)+1
    for i in range(2,int(y)):
        if x%i==0:
            return False
    return True   
arr=[]
for i in range(P+1,S):
    if isPrime(i):
        arr.append(i)
        
print(arr)



set=[]
def backtracking(sum,comb,arr,index,N,S):
  
    if sum==S and len(comb)==N:
            print(comb)
            return 
    if sum>S or index==len(arr):
            return

    sum=sum+arr[index]
    comb.append(arr[index])
    backtracking(sum,comb,arr,index+1,N,S)
    sum=sum-arr[index]
    comb.pop()
    backtracking(sum,comb,arr,index+1,N,S)
    


backtracking(0,[],arr,0,N,S)
              
                                          
