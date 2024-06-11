grid = [[0,6,0],
        [5,8,7],
        [0,9,0]
       ]

def f(grid,r,c,sum):
    if r < 0 or r == len(grid) or c < 0 or c == len(grid[0])  or grid[r][c] == 0:
         return 0
    temp=grid[r][c]
    grid[r][c]=0
    

    
    if r>0:
         #go up
         y=y+f(grid,r-1,c)

    if c>0:
         #go left
         y=y+f(grid,r,c-1)
    if r<len(grid)-1:
         #go down
         y=y+f(grid,r+1,c)
    if c<len(grid[0])-1:
         #go right
         y=y+f(grid,r,c+1)

    return temp+y   
  
print(f(grid,0,1,0))            
                   


