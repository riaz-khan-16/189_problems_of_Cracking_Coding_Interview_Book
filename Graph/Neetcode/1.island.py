#https://leetcode.com/problems/number-of-islands/

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

rows=len(grid)
cols=len(grid[0])
count=0
visited=set()

def bfs(row,col):
    
    queue=[(row,col)]
    visited.add((row,col))
    while queue:
      x,y=queue.pop(0)
      directions=[[0,1],[1,0],[-1,0],[0,-1]]
      for i,j in directions:
          if 0<=(x+i)<len(grid) and 0<=(y+j)<len(grid[0]):
            if grid[x+i][y+j]=='1' and (x+i,y+j) not in visited:
                queue.append((x+i,y+j))
                visited.add((x+i,y+j))
        
        
for i in range(rows):
    for j in range(cols):
        if grid[i][j]=='1' and (i,j) not in visited:
            bfs(i,j)
            count=count+1
print(count)
