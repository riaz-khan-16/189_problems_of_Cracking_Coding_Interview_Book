
m=3
n=4
matrix=[]
def make_matrix(row,col,matrix):
        col=[-1]*(col)
        
        for i in range(row):
            matrix.append(col)
        return matrix

       
wt=[1,3,4,5]
val=[1,4,5,7]
W=10

matrix=make_matrix(n+1,W+1,[])
print(matrix)

def knapscak(wt,val,W,n):
    # base condition

    if n==0 or W==0:
        return 0
    if matrix[n][W]!=-1:
         return matrix[n][W]
    if wt[n-1]<=W:
        matrix[n][W]= max(val[n-1]+ knapscak(wt,val,W-wt[n-1],n-1),knapscak(wt,val,W,n-1))
        return matrix[n][W]
    if wt[n-1]>W:
        matrix[n][W]=knapscak(wt,val,W,n-1)
        return matrix[n][W]

n=len(wt)
print(knapscak(wt,val,W,n))