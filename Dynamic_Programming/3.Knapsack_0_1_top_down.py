
m=3
n=4
matrix=[]
def make_matrix(row,col,matrix):
        col=[0]*(col)
        
        for i in range(row):
            matrix.append(col)
        return matrix

       
wt=[1,3,4,5]
val=[1,4,5,7]
W=7

matrix=make_matrix(n+1,W+1,[])
print(matrix)

def knapscak(wt,val,W,n):
    # base condition
    for i in range(n+1):
         for j in range(W+1):
               # base condition
               if n==0 or W==0:
                    matrix[i][j]=0

               elif wt[i-1]<=j:
                      matrix[i][j]= max(val[i-1]+ matrix[i-1][j-wt[i-1]] ,matrix[i-1][j])
               elif wt[i-1]>j:
                    matrix[i][j]=matrix[i-1][j]
                         
    print(matrix[n][W])
    
knapscak(wt,val,W,n)