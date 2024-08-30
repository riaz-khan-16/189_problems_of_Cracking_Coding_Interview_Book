# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0. 



matrix=[[1, 2, 3],[3, 0, 5], [6, 7, 8]]

zero=[]
#find zero
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==0:
           zero.append([i,j])

print(zero)
row=zero[0][0]
column=zero[0][1]


#make the row zero
for k in range(len(matrix[0])):
    matrix[row][k]=0
    print(row,k)

print(matrix)

#make the column zero
for l in range(len(matrix[0])):
    matrix[l][column]=0

print(matrix)