# 64. Minimum Path Sum

grid = [[1,3,1],[1,5,1],[4,2,1]]
row_lenth=len(grid)-1
col_lenth=len(grid[0])-1

memo={}
def dp(row,col):
    if (row,col) in memo:
          return memo[(row,col)]
    
    if row == row_lenth and col == col_lenth:
            return grid[row][col]
    
    if row==row_lenth:
          return grid[row][col]+dp(row,col+1)
    if col==col_lenth:
          return grid[row][col]+dp(row+1,col)
    
    right = dp(row, col + 1)
    down = dp(row + 1, col)
    memo[(row,col)]=grid[row][col] + min(right, down)
        
    return grid[row][col] + min(right, down)


      


    
  
     

print(dp(0,0))
    
    
    
